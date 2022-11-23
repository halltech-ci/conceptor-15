# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    print_line = fields.Boolean(string="Print", default=True)
    sale_uom = fields.Many2one('sale.uom', string='Unité')