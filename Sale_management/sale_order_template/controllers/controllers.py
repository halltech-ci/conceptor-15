# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderTemplate(http.Controller):
#     @http.route('/sale_order_template/sale_order_template', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_template/sale_order_template/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_template.listing', {
#             'root': '/sale_order_template/sale_order_template',
#             'objects': http.request.env['sale_order_template.sale_order_template'].search([]),
#         })

#     @http.route('/sale_order_template/sale_order_template/objects/<model("sale_order_template.sale_order_template"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_template.object', {
#             'object': obj
#         })
