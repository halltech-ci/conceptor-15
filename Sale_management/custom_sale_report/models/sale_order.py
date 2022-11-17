# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SalOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    print_line = fields.Boolean(string="Print", default=True)