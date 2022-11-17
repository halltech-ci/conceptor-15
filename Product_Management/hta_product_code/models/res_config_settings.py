# -*- coding: utf-8 -*-

from odoo import fields, models


class BaseConfiguration(models.TransientModel):
    _inherit = "res.config.settings"

    group_product_default_code_manual_mask = fields.Boolean(
        string="Product Default Code Manual Mask",
        default=False,
        help="Set behaviour of codes. Default: Automask"
        " (depends on variant use: "
        "see Sales/Purchases configuration)",
        implied_group="hta_product_code"
        ".group_product_default_code_manual_mask",
    )

    prefix_as_default_code = fields.Boolean(
        string="Reference Prefix as default Reference",
        default=False,
        config_parameter="hta_product_code.prefix_as_default_code",
    )