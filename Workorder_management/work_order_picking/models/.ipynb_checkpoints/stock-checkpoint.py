# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    work_order_id = fields.Many2one('work.order')
    
    
class StockMove(models.Model):
    _inherit = 'stock.move'
    
    product_line_id = fields.Many2one('product.line', string='Product Line')