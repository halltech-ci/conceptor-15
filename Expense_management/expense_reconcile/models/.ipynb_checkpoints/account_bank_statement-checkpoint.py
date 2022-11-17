# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"
    
    
    move_id = fields.Many2one('account.move')