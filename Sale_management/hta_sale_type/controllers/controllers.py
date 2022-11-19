# -*- coding: utf-8 -*-
# from odoo import http


# class HtaSaleType(http.Controller):
#     @http.route('/hta_sale_type/hta_sale_type', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hta_sale_type/hta_sale_type/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hta_sale_type.listing', {
#             'root': '/hta_sale_type/hta_sale_type',
#             'objects': http.request.env['hta_sale_type.hta_sale_type'].search([]),
#         })

#     @http.route('/hta_sale_type/hta_sale_type/objects/<model("hta_sale_type.hta_sale_type"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hta_sale_type.object', {
#             'object': obj
#         })
