# -*- coding: utf-8 -*-
# from odoo import http


# class WorkOrderAnalytic(http.Controller):
#     @http.route('/work_order_analytic/work_order_analytic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/work_order_analytic/work_order_analytic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('work_order_analytic.listing', {
#             'root': '/work_order_analytic/work_order_analytic',
#             'objects': http.request.env['work_order_analytic.work_order_analytic'].search([]),
#         })

#     @http.route('/work_order_analytic/work_order_analytic/objects/<model("work_order_analytic.work_order_analytic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('work_order_analytic.object', {
#             'object': obj
#         })
