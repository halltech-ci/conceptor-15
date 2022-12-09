# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ResCompany(models.Model):
    _inherit='res.company'
    
    wo_picking_source = fields.Many2one('stock.location')
    wo_picking_dest = fields.Many2one('stock.location')
    wo_picking_type = fields.Many2one('stock.picking.type', string='Operation types')