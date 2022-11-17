# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ExpenseRequest(models.Model):
    _inherit = 'expense.request'
    
    analytic_account = fields.Many2one('account.analytic.account', string='Analytic Account', check_company=True,)
    
    
class ExpenseLine(models.Model):
    _inherit = "expense.line"
    
    analytic_account = fields.Many2one('account.analytic.account', string='Analytic Account', related='request_id.analytic_account')