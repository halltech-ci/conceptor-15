# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'
    
    product_line = fields.One2many('product.line', 'analytic_line', string="Product line")
