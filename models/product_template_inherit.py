# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _, SUPERUSER_ID




class ProductTemplate(models.Model):
    _inherit = "product.template"


    # @api.onchange('list_price')
    # def _onchange_list_price(self):
    #     if self.list_price:
    #         self.list_price = self.list_price + self.taxes_id.amount