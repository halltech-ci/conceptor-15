# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    work_order_id = fields.Many2one('work.order')
    
    def button_validate(self):
        self.work_order_id._action_done()
        return super(StockPicking, self).button_validate()
    
    
class StockMove(models.Model):
    _inherit = 'stock.move'
    
    product_line_id = fields.Many2one('product.line', string='Product Line')