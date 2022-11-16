# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WorkOrder(models.Model):
    _inherit = 'work.order'
    
    account_analytic_id = fields.Many2one('account.analytic.account', related='project_id.analytic_account_id')
    
    
class ProductLine(models.Model):
    _inherit = 'product.line'
    
    
    analytic_line = fields.Many2one('account.analytic.line', string="Analytic line")