# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WorkOrder(models.Model):
    _inherit = 'work.order'
    
    @api.model
    def _get_default_picking_type(self):
        company_id = self.env.context.get('default_company_id', self.env.company.id)
        return self.env['stock.picking.type'].search([('code', '=', 'internal'), ('warehouse_id.company_id', '=', company_id), ], limit=1)
    
    @api.model
    def _get_default_location_src_id(self):
        location = False
        company_id = self.env.context.get('default_company_id', self.env.company.id)
        if self.env.context.get('default_picking_type_id'):
            location = self.env['stock.picking.type'].browse(self.env.context['default_picking_type_id']).default_location_src_id
        if not location:
            location = self.env['stock.warehouse'].search([('company_id', '=', company_id)], limit=1).lot_stock_id
        return location and location.id or False

    @api.model
    def _get_default_location_dest_id(self):
        location = False
        company_id = self.env.context.get('default_company_id', self.env.company.id)
        if self._context.get('default_picking_type_id'):
            location = self.env['stock.picking.type'].browse(self.env.context['default_picking_type_id']).default_location_dest_id
        if not location:
            location = self.env['stock.warehouse'].search([('company_id', '=', company_id)], limit=1).lot_stock_id
        return location and location.id or False
    
    picking_type = fields.Many2one('stock.picking.type', 'Picking Type', default=_get_default_picking_type, )
    location_src_id = fields.Many2one("stock.location", string="Emplacement Source", required=True, default=_get_default_location_src_id, domain="[('usage','=','internal'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]",)
    location_dest_id = fields.Many2one(string="Destination", comodel_name="stock.location", required=True, default=_get_default_location_dest_id, domain="[('usage','=','internal'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]",)
    picking_ids = fields.One2many('stock.picking', 'work_order_id', string="Stock")
    picking_count = fields.Integer(string='Picking Orders', compute='_compute_picking_ids', default=0)
    picking_type = fields.Many2one('stock.picking.type', 'Picking Type', default=_get_default_picking_type, )
    
    @api.depends('picking_ids')
    def _compute_picking_ids(self):
        for rec in self:
            rec.picking_count = len(rec.picking_ids)
            
    def action_view_picking(self):
        '''
        This function returns an action that display existing delivery orders
        of given work order ids. It can either be a in a list or in a form
        view, if there is only one delivery order to show.
        '''
        action = self.env.ref('stock.action_picking_tree_all').read()[0]

        pickings = self.mapped('picking_ids')
        if len(pickings) > 1:
            action['domain'] = [('id', 'in', pickings.ids)]
        elif pickings:
            form_view = [(self.env.ref('stock.view_picking_form').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [(state,view) for state,view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = pickings.id
        # Prepare the context.
        picking_id = pickings.filtered(lambda l: l.picking_type_id.code == 'outgoing')
        if picking_id:
            picking_id = picking_id[0]
        else:
            picking_id = pickings[0]
        action['context'] = dict(self._context, default_picking_type_id=picking_id.picking_type_id.id, default_origin=self.name, default_group_id=picking_id.group_id.id)
        return action
    
    def action_confirm(self):
        if not self.button_approve():
            raise ValidationError(_("You must approve this request before"))
        if len(self.picking_ids) > 0:
            raise ValidationError(_("You can not confirm request that is already confirm"))
        self._create_picking()
        return True
    
    
    def _get_picking_value(self):
        origin = self.name
        date = self.date_approve
        picking_value = {
            'picking_type_id': self.picking_type_id.id,
            'location_id':self.picking_type_id.default_location_src_id.id,
            'location_dest_id': rec.location_dest_id.id,
            'origin': origin,
            'company_id': self.company_id.id,
            'date': date,
        }
        return picking_value
    
    def _get_move_value(self):
        lines = self.mapped('line_ids')
        move_value = []
        for line in lines:
            description_picking = line.product_id.with_context(lang=request.project_id.partner_id.lang or self.env.user.lang)._get_description(request.picking_type_id)
            moves = (0, 0, {
                'name': line.product_id.display_name,
                'product_id': line.product_id.id,
                'description_picking': description_picking,
                'product_uom_qty': line.product_uom_qty,
                'product_uom': line.product_uom_id.id,
                'location_id': self.location_src_id.id,
                'location_dest_id': self.location_dest_id.id,
                'price_unit': line.product_id.standard_price,
                'product_line_id': line.id,
                'company_id': self.company_id.id,
                'origin': line.order_id.name,
                    }
                )
            move_value.append(moves)
        return move_value
          
    def _create_picking(self):
        for rec in self:
            picking_value = rec._get_picking_value()
            move = rec._get_move_value()
            picking = self.env['stock.picking'].create(picking_value)
            picking.write({'move_lines': move,})
            picking.action_confirm()
        return True
            
    '''
    def _create_picking(self):
        self.ensure_one()
        for request in self:
            #prepare picking
            picking_type_id = request.picking_type_id
            location_id = request.location_src_id
            location_dest_id = request.location_dest_id
            origin = request.name
            company_id = request.company_id
            date = request.date_approve
            picking_value = {
                'picking_type_id': picking_type_id.id,
                #'location_id': location_id.id,
                'origin': origin,
                'company_id': self.company_id.id,
                'date': date,
                'location_id':picking_type_id.default_location_src_id.id,
                'location_dest_id': location_dest_id.id
            }
            picking = self.env['stock.picking'].create(picking_value)
            move_value = []
            move_line_value = []
            product_lines = request.mapped('line_ids')
            for line in product_lines:
                #create stock_move (move_lines)
                description_picking = line.product_id.with_context(lang=request.project_id.partner_id.lang or self.env.user.lang)._get_description(request.picking_type_id)
                moves = (0, 0, {
                    'name': line.product_id.display_name,
                    'product_id': line.product_id.id,
                    'description_picking': description_picking,
                    'product_uom_qty': line.product_uom_qty,
                    'product_uom': line.product_uom_id.id,
                    'location_id': location_id.id,
                    'location_dest_id':location_dest_id.id,
                    'price_unit': line.product_id.standard_price,
                    'product_line_id': line.id,
                    'company_id': self.company_id.id,
                    'origin': origin,
                        }
                    )
                move_value.append(moves)
            picking.write({'move_lines': move_value,})
            picking.action_confirm()
            #request._action_done()
        return True'''



class ProductLine(models.Model):
    _inherit = 'product.line'
    
    move_ids = fields.One2many('stock.move', 'product_line_id', string='Reservation', readonly=True, ondelete='set null', copy=False)
    
    