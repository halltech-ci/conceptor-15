# -*- coding: utf-8 -*-

from odoo import models, fields, api


REQUEST_STATE = [
        ('draft', 'Brouillon'),
        ('submit', 'En attente'),
        ('validate', 'Valide'),
        ('to_approve', 'A approuver'),
        ('approve', 'Approuve'),
        ('authorize','Autorise'),
        ('to_cancel', 'Annule'),
        ('post', 'Paye'),
        ('reconcile', 'Lettre'),
        ('cancel', 'Rejete')
    ]

class ExpenseLine(models.Model):
    _name ='expense.line'
    _description = 'Custom expense line'
    
    
    @api.model
    def _default_employee_id(self):
        return self.env.user.employee_id
    
    @api.model
    def _get_analytic_domain(self):
        project_ids = self.env['project.project'].search([]).ids
        res = [('project_ids', 'not in', project_ids)]
        return res
    
    @api.model
    def _get_employee_id_domain(self):
        employee_ids = self.env['hr.employee'].search([]).ids
        res = [('address_home_id.property_account_payable_id', '!=', False), ('id', 'in', employee_ids)]
        return res
    
    
    name = fields.Char('Description', required=True)
    request_state = fields.Selection(selection=REQUEST_STATE, string='Status', index=True, readonly=True, copy=False, default='draft', required=True, help='Expense Report State')
    employee_id = fields.Many2one('hr.employee', string="Beneficiaire", required=True, check_company=True,)
    request_id = fields.Many2one('expense.request', string='Expense Request')
    date = fields.Datetime(readonly=True, related='request_id.date', string="Date")
    amount = fields.Float("Montant", required=True, digits='Product Price')
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True, default=lambda self: self.env.company)
    requested_by = fields.Many2one('res.users' ,'Demandeur', related='request_id.requested_by')
    expense_type = fields.Boolean(string="Imputer au projet", default=True)
    currency_id = fields.Many2one('res.currency', string='Currency', readonly=True, default=lambda self: self.env.company.currency_id)
    accounting_date = fields.Date(string='Accounting Date')
    extra_fees = fields.Float('Frais annexes', digits='Product Price')
    
    
    def _get_statement_line(self):
        line = {
            'payment_ref': self.name,
            'amount': self.amount if self.amount < 0 else -self.amount,
            'expense_id': self.request_id.id,
            'credit_account': self.request_id.journal.default_account_id.id,
            'company_id' : self.company_id.id,
        }
        return line
    
    
    def action_submit(self):
        self._action_submit()

    def _action_submit(self):
        self.request_state = "submit"
        
    def action_to_approve(self):
        self.request_state = "to_approve"
    
    def action_approve(self):
        self.request_state = "approve"  
    
    def to_approve(self):
        self.request_state = "validate"
    
    def action_authorize(self):
        self.request_state = "authorize"
    
    def action_post(self):
        self.request_state = "post"
    
    def action_validate(self):
        self.request_state = "validate"
        
    def do_cancel(self):
        """Actions to perform when cancelling a expense line."""
        self.write({"request_state": 'draft'})
    
    def unlink(self):
        for expense in self:
            if expense.request_state in ['post',]:
                raise UserError(_('Vous ne pouvez pas supprimer une dépense déja payée'))
        return super(ExpenseLine, self).unlink()

    def write(self, vals):
        return super(ExpenseLine, self).write(vals)