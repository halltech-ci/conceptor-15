# -*- coding: utf-8 -*-

from odoo import models, fields, api


REQUEST_STATE = [('draft', 'Draft'),
        ('submit', 'Submitted'),
        ('to_approve', 'To Approve'),
        ("open", "In progress"),
        ('done', 'Done'),
        ('close', 'Closed'),
        ('cancel', 'Refused')
        ]


class WorkOrderLine(models.Model):
    _name = "work.order.line"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Manage product for work order"
    
    
    name = fields.Char(string="Description")
    request_state = fields.Selection(string='Status', copy=False, related="order_id.state",)
    order_id = fields.Many2one('work.order', string="Product Request")
    product_id = fields.Many2one("product.product", string="Product", domain=[("purchase_ok", "=", True)],)
    product_uom_id = fields.Many2one("uom.uom", string="Product Unit of Measure", related='product_id.uom_id')
    initial_qty = fields.Float('Initial Qty', digits="Product Unit of Measure")#Quantity in sale order
    product_uom_qty = fields.Float('Product Qty', digits="Product Unit of Measure")#Quantity ask for workorder
    qty_done = fields.Float('Qty Done', digits="Product Unit of Measure", compute='_compute_qty_done',)#Quantity give by stock
    qty_in_progress = fields.Float(string="Qty In Progress", digits="Product Unit of Measure", readonly=True, store=True,
        help="Quantity in progress. Qty left", default=0) 
    project_id = fields.Many2one('project.project', related="order_id.project_id")
    task_id = fields.Many2one('project.task', related="order_id.task_id")
    
    
    def action_to_approve(self):
        self.request_state = "to_approve"
    
    def action_approve(self):
        self.request_state = "open"
    
    def action_done(self):
        self.request_state = "done"
    
    def set_to_draft(self):
        self.request_state = 'draft'
        
    def action_close(self):
        self.request_state = 'close'
    