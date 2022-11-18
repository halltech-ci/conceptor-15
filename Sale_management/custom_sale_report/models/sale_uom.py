# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleUom(models.Model):
    _name = "sale.uom"
    _description = "Unite de mesure de vente"
    
    
    name = fields.Char(string="Nom")
    code = fields.Char(string="Symbole")