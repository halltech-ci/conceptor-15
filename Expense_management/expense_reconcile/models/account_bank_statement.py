# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"
     
    move_id = fields.Many2one('account.move')
    expense_state = fields.Selection(related="expense_id.state", string='Expense State')
    
    
    def _create_debit_line(self):
        return {
                'name': self.name,
                'account_id': self.debit_account.id,
                'debit': self.amount < 0.0 and -self.amount or 0.0,#line.amount < 0.0 and line.amount or 0.0
                'credit': self.amount > 0.0 and self.amount or 0.0, #line.amount > 0.0 and abs(line.amount)
                'partner_id': self.partner_id.id,
                'journal_id': self.expense_id.journal.id,
                'date': fields.Date.today(),
                'statement_id': self.statement_id.id,
                'statement_line_id': self.id,
            }
    
    def _create_credit_line(self):
        return {
                'name': self.name,
                'account_id': self.expense_id.journal.default_account_id.id,
                'debit': self.amount > 0.0 and self.amount or 0.0,
                'credit': self.amount < 0.0 and -self.amount or 0.0, 
                'partner_id': self.partner_id.id,
                'journal_id': self.expense_id.journal.id,
                'date': fields.Date.today(),
                'statement_id': self.statement_id.id,
                'statement_line_id': self.id,
            }