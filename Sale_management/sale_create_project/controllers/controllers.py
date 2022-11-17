# -*- coding: utf-8 -*-
# from odoo import http


# class SaleCreateProject(http.Controller):
#     @http.route('/sale_create_project/sale_create_project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_create_project/sale_create_project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_create_project.listing', {
#             'root': '/sale_create_project/sale_create_project',
#             'objects': http.request.env['sale_create_project.sale_create_project'].search([]),
#         })

#     @http.route('/sale_create_project/sale_create_project/objects/<model("sale_create_project.sale_create_project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_create_project.object', {
#             'object': obj
#         })
