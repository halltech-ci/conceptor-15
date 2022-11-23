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
            rec.write({'project_id': project.id, 'state':'sale',})
        return project
    