# -*- coding: utf-8 -*-

from odoo import models, fields, api



REQUEST_STATES = [
    ("draft", "Draft"),
    ("to_approve", "To Approve"),
    ("open", "In progress"),
    ("done", "Done"),
    ('close', 'Closed'),
    ("cancel", "Cancelled"),
]

class WorkorderRequest(models.model):
    _name ="workorder.request"
    _description = "Manage work order"
    
    
    name = fields.Char(string="Request Reference", required=True, tracking=True, default='/', readonly=True)
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company, index=True, required=True, readonly=True)
    state = fields.Selection(selection=REQUEST_STATES, string="Status", copy=False, default="draft", index=True, readonly=True, tracking=True)
    date = fields.Datetime(readonly=True, default=fields.Datetime.now, string="Date")
    
    
    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            if 'company_id' in  vals:
                vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code('order.request') or '/'
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('order.request') or '/'
        request = super(WorkorderRequest, self).create(vals)
        return request
    
    def write(self, vals):
        res = super(WorkorderRequest, self).write(vals)
        return res
    
    def unlink(self):
        for request in self:
            if request.state in ('close', 'done'):
                raise UserError(_('Vous ne pouvez pas supprimer un OT déja traité.'))
        return super(WorkorderRequest, self).unlink()