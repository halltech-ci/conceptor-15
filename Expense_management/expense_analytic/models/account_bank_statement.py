# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"
    
    
    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account', ondelete='set null')
    analytic_tag_ids = fields.Many2many('account.analytic.tag', string='Analytic Tags', relation='account_statement_model_analytic_tag_rel')
    
    def _create_debit_line(self):
        vals = super(AccountBankStatementLine, self)._create_debit_line()
        vals['analytic_account_id'] = self.analytic_account_id
        return vals