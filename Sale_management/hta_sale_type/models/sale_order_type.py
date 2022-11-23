# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrderType(models.Model):
    _name = "sale.order.type"
    _description = "Manage sale order type"
    _check_company_auto = True
    
    
    name = fields.Char(required=True, translate=True)
    code = fields.Char()
    company_id = fields.Many2one("res.company", default=lambda self: self.env.company, store=True,)
    active = fields.Boolean(string="Active", default=True)