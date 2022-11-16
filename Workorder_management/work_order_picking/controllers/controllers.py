# -*- coding: utf-8 -*-
# from odoo import http


# class WorkOrderPicking(http.Controller):
#     @http.route('/work_order_picking/work_order_picking', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/work_order_picking/work_order_picking/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('work_order_picking.listing', {
#             'root': '/work_order_picking/work_order_picking',
#             'objects': http.request.env['work_order_picking.work_order_picking'].search([]),
#         })

#     @http.route('/work_order_picking/work_order_picking/objects/<model("work_order_picking.work_order_picking"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('work_order_picking.object', {
#             'object': obj
#         })
