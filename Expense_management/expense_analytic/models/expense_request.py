# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ExpenseRequest(models.Model):
    _inherit = 'expense.request'
    
    analytic_account = fields.Many2one('account.analytic.account', string='Analytic Account', check_company=True,)
    
    def create_bank_statement(self):
        res = super(ExpenseRequest, self).create_bank_statement()
        return res    
    
    
class ExpenseLine(models.Model):
    _inherit = "expense.line"
    
    analytic_account = fields.Many2one('account.analytic.account', string='Analytic Account', related='request_id.analytic_account')
    
    def _get_statement_line(self):
        vals = super(ExpenseLine, self)._get_statement_line()
        vals['analytic_account'] = self.analytic_account
        return vals