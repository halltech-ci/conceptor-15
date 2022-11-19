# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleUom(models.Model):
    _name = "sale.uom"
    _description = "Unite de mesure de vente"
        
    name = fields.Char(string="Nom", required=True)
    code = fields.Char(string="Symbole")
    
    def create(self, vals):
        result = super(SaleUom, self).create(vals)
        return result
    
    def unlink(self):
        return super(SaleUom, self).unlink()