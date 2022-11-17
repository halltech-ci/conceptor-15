# -*- coding: utf-8 -*-
# from odoo import http


# class ExpenseReconcile(http.Controller):
#     @http.route('/expense_reconcile/expense_reconcile', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/expense_reconcile/expense_reconcile/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('expense_reconcile.listing', {
#             'root': '/expense_reconcile/expense_reconcile',
#             'objects': http.request.env['expense_reconcile.expense_reconcile'].search([]),
#         })

#     @http.route('/expense_reconcile/expense_reconcile/objects/<model("expense_reconcile.expense_reconcile"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('expense_reconcile.object', {
#             'object': obj
#         })
