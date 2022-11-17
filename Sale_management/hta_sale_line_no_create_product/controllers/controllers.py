# -*- coding: utf-8 -*-
# from odoo import http


# class HtaSaleLineNoCreateProduct(http.Controller):
#     @http.route('/hta_sale_line_no_create_product/hta_sale_line_no_create_product', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_sale_line_no_create_product/hta_sale_line_no_create_product/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_sale_line_no_create_product.listing', {
#             'root': '/hta_sale_line_no_create_product/hta_sale_line_no_create_product',
#             'objects': http.request.env['hta_sale_line_no_create_product.hta_sale_line_no_create_product'].search([]),
#         })

#     @http.route('/hta_sale_line_no_create_product/hta_sale_line_no_create_product/objects/<model("hta_sale_line_no_create_product.hta_sale_line_no_create_product"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_sale_line_no_create_product.object', {
#             'object': obj
#         })
