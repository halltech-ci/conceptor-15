# -*- coding: utf-8 -*-
# from odoo import http


# class ExpenseAnalytic(http.Controller):
#     @http.route('/expense_analytic/expense_analytic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/expense_analytic/expense_analytic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('expense_analytic.listing', {
#             'root': '/expense_analytic/expense_analytic',
#             'objects': http.request.env['expense_analytic.expense_analytic'].search([]),
#         })

#     @http.route('/expense_analytic/expense_analytic/objects/<model("expense_analytic.expense_analytic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('expense_analytic.object', {
#             'object': obj
#         })
