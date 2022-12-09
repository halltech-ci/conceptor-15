# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfigSttings(models.TransientModel):
    _inherit = "res.config.settings"
    
    
    wo_picking_source = fields.Many2one('stock.location', related='company_id.wo_picking_source')
    wo_picking_dest = fields.Many2one('stock.location', related='company_id.wo_picking_dest')
    wo_picking_type = fields.Many2one('stock.picking.type', string='Operation types', related="company_id.wo_picking_type")