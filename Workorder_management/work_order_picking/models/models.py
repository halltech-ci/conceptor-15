# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class work_order_picking(models.Model):
#     _name = 'work_order_picking.work_order_picking'
#     _description = 'work_order_picking.work_order_picking'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
