# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.http import request


class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    
    state = fields.Selection(selection_add=[
        ('waiting_for_approval', 'Attente de validation'),
        ('approve', 'Approuve'),
        ('sent',),
        ]
    )
    approver_id = fields.Many2one('res.users', string="Approbateur")
    
    def ask_for_approval(self):
        for rec in self:
            if not rec.approver_id:
                raise UserError(_('Veuillez choisir un approbateur.'))
            self.send_mail_to_approver()
            rec.state = 'waiting_for_approval'
    
    def action_approve(self):
        for rec in self:
            rec.state = 'approve'
    
    def action_quotation_send(self):
        res = super(SaleOrder,self).action_quotation_send()
        if res:
            for rec in self:
                rec.state = 'sent'
        return res
            
            
    def send_mail_to_approver(self):
        subject = 'Devis: Demande de validation'
        recipients = self.approver_id.email
        base_url = request.env['ir.config_parameter'].get_param('web.base.url')
        base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
        message = "<p>Cher(e) {0}</p>".format(self.approver_id.name) + "<p>Vous avez une demande de validation en attente {0}</p>".format(self.name) + "<p>Cliquer sur le lien pour valider</p>"
        message_body = message + base_url
        template_obj = self.env['mail.mail']
        template_data = {
            'subject': subject,
            'body_html': message_body,
            'email_to': recipients
        }
        template_id = template_obj.create(template_data)
        template_obj.send(template_id)
        template_id.send()
        return True 