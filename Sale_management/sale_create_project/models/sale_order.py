# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    create_project = fields.Selection(selection=[('add_to_project', "Use project"), ('create_project', "Create Project"),], default='add_to_project')
    description = fields.Text(string="Decription")
    has_project = fields.Boolean(compute = '_compute_has_project_id', store=True,)
    analytic_group = fields.Many2one('account.analytic.group', string='Groupe Analytic')
    project_id = fields.Many2one('project.project', copy=False)
    
    @api.depends('project_id')
    def _compute_has_project_id(self):
        for rec in self:
            if rec.project_id:
                rec.has_project = True
            else:
                rec.has_project = False
    
    def action_done(self):
        res = super(SaleOrder, self).action_done()
        self.write({'project_id': self.project_id.id})
        return res
    
    def create_task_from_line(self):
        lines = self.order_line.filtered(lambda l:l.is_task == True)
        if lines:
            for line in lines:
                value = line._generate_task_value()
                self.env['project.task'].create(value)
        else:
            pass
    
    
    def create_project_sale_confirm(self):
        """ Generate project for the given so, and link it.
            :param project or project template: record of project.project in which the task should be created
            :return task: record of the created task
        """
        self.ensure_one()
        for rec in self:
            if rec.create_project in ('add_to_project'):
                project = rec.project_id
            if rec.create_project == "create_project":
                account = rec.analytic_account_id
                if not account:
                    rec._create_analytic_account(prefix=rec.description or rec.name or None)
                    account = rec.analytic_account_id
                account.write({'group_id': rec.analytic_group})
                values = {
                    'name': rec.description or rec.name,
                    'analytic_account_id': account.id,
                    'partner_id': rec.partner_id.id,
                    'sale_order_id': rec.id,
                    'active': True,
                    'company_id': rec.company_id.id,
                }
                project = self.env['project.project'].create(values)
            rec.write({'project_id': project.id, 'state':'done',})
            rec.create_task_from_line()
        return project
    
    
    
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    is_task = fields.Boolean(string='Task', default=False)
    
    def _generate_task_value(self):
        project = self.order_id.project_id
        return {
            'name': '%s: %s' % (self.order_id.name, self.name),
            'partner_id': self.order_id.partner_id.id,
            'email_from': self.order_id.partner_id.email,
            'project_id': project.id,
            'sale_line_id': self.id,
            'sale_order_id': self.order_id.id,
            'company_id': project.company_id.id,
            'user_ids': False,  # force non assigned task, as created as sudo()
        }
    