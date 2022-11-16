# -*- coding: utf-8 -*-

from odoo import models, fields, api



REQUEST_STATES = [
    ("draft", "Draft"),
    ("to_approve", "To Approve"),
    ("open", "En Cours"),
    ("confirm", "Confirm"),
    ("done", "Done"),
    ('close', 'Closed'),
    ("cancel", "Cancelled"),
]

class WorkOrder(models.Model):
    _name ="work.order"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _check_company_auto = True
    _description = "Manage work order"
    
    
    @api.model
    def _get_default_requested_by(self):
        return self.env["res.users"].browse(self.env.uid)
        
    
    name = fields.Char(string="Request Reference", required=True, tracking=True, default='/', readonly=True)
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company, index=True, required=True, readonly=True)
    state = fields.Selection(selection=REQUEST_STATES, string="Status", copy=False, default="draft", index=True, readonly=True, tracking=True)
    date = fields.Datetime(readonly=True, default=fields.Datetime.now, string="Date")
    project_id = fields.Many2one('project.project', string="Project", check_company = True, tracking=True)
    task_id = fields.Many2one('project.task', string="Project Task",)
    requested_by = fields.Many2one("res.users", string="Requested by", required=True, copy=False, tracking=True, default=_get_default_requested_by, index=True, readonly=True,)
    line_ids = fields.One2many(comodel_name="product.line", inverse_name="order_id", string="Products", copy=True, tracking=True,)
    date_approve = fields.Datetime('Date Approve', readonly=1, index=True, copy=False)
    
    
    def button_to_approve(self):
        for line in self.line_ids:
            line.action_to_approve()
        return self.write({"state": "to_approve"})
    
    def set_to_draft(self):
        if self.state in ['done', 'close']:
            raise ValidationError(_("Vous ne pouvez pas reinitialiser un OT déja traité"))
        for line in self.line_ids:
            line.set_to_draft()
        self.write({'state': 'draft'})
           
    def button_approve(self):
        for line in self.line_ids:
            line.action_approve()
        self.write({"state": "open", 'date_approve': fields.Datetime.now()})
        return True
    
    def action_confirm(self):
        if not self.button_approve():
            raise ValidationError(_("You must approve this request before"))
        if len(self.picking_ids) > 0:
            raise ValidationError(_("You can not confirm request that is already confirm"))
        self._create_picking()
        return True
    
    def _action_done(self):
        for line in self.line_ids:
            line.action_done()
        return self.write({"state": 'done'})
    
    
    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            if 'company_id' in  vals:
                vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code('work.order') or '/'
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('work.order') or '/'
        request = super(WorkOrder, self).create(vals)
        return request
    
    def write(self, vals):
        res = super(WorkOrder, self).write(vals)
        return res
    
    def unlink(self):
        for request in self:
            if request.state in ('close', 'done'):
                raise UserError(_('Vous ne pouvez pas supprimer un OT déja traité.'))
        return super(WorkOrder, self).unlink()