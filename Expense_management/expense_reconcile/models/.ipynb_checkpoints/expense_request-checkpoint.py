# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ExpenseRequest(models.Model):
    _inherit = 'expense.request'
    
    move_ids = fields.Many2many('account.move', string='Account Move')
    
    
    def create_move_values(self):
        self.ensure_one()
        for request in self:
            account_src = request.journal.default_account_id.id
            ref = request.statement_id.name
            journal = request.journal
            company = request.company_id
            account_date = fields.Date.today()
            lines = request.mapped('statement_line_ids')
            move_lines = []
            for line in lines:
                partner = line.partner_id
                debit_account = line.debit_account
                move_value = {
                    'ref': ref,
                    'date': account_date,
                    'journal_id': journal.id,
                    'company_id': company.id,
                }
                debit_line = (0, 0, {
                    'name': line.name,
                    'account_id': debit_account.id,
                    'debit': line.p_amount > 0.0 and -line.amount or 0.0,#line.amount < 0.0 and line.amount or 0.0
                    'credit': line.p_amount < 0.0 and line.amount or 0.0, #line.amount > 0.0 and abs(line.amount)
                    'partner_id': partner.id,
                    'journal_id': journal.id,
                    'date': account_date,
                    'statement_id': self.statement_id.id,
                    'statement_line_id': line.id,
                })
                move_lines.append(debit_line)
                credit_line = (0, 0, {
                    'name': line.name,
                    'account_id': account_src,
                    'debit': line.p_amount < 0.0 and line.amount or 0.0,
                    'credit': line.p_amount > 0.0 and -line.amount or 0.0, 
                    'partner_id': partner.id,
                    'journal_id': journal.id,
                    'date': account_date,
                    'statement_id': self.statement_id.id,
                    'statement_line_id': line.id,
                })
                move_lines.append(credit_line)
                move_value['line_ids'] = move_lines
                move = self.env['account.move'].create(move_value)
            for line in lines:
                line.write({'move_id': move.id})
            move.post()
            request.write({'state': 'reconcile'})
        return True
    
    
class ExpenseLine(models.Model):
    _inherit ='expense.line'
    
    partner_id = fields.Many2one('res.partner', string="Fournisseur")