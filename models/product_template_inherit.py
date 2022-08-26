# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _, SUPERUSER_ID




class ProductTemplate(models.Model):
    _inherit = "product.template"

    list_price = fields.Float(
        'Sales Price', default=1.0,
        digits='Product Price', compute="_compute_price_ttc"
    )

    def _compute_price_ttc(self):
        if self.list_price and self.taxes_id:
            self.list_price = self.list_price + self.taxes_id.amount
        return self.list_price