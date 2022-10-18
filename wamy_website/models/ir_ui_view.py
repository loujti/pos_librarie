import logging
from odoo import api, fields, models
_logger = logging.getLogger(__name__)
from odoo.http import request
from odoo.addons import website


class View(models.Model):
    _inherit = "ir.ui.view"
    
    website_published = fields.Boolean(string='website_published')
    
    @api.model
    def _prepare_qcontext(self):
        qcontext = super(View, self)._prepare_qcontext()
        partner_pictures = self.env['res.partner'].sudo().search([('website_published', '=', True)])
        my_statistics = self.env['wamy.website.statistics'].sudo().search([])
        list = []
        listf = []
        for pic in  [partner_pictures, my_statistics, ]:
            list.append(pic)
            if len(list) == 4:
                listf.append(list)
                list = []
        
        qcontext.update(dict(
            self._context.copy(),
            partner_pictures=listf if len(listf) > 0 else False,
            my_statistics=listf if len(listf) > 0 else False,
            
        ))
        # Add Menu Visibility State
        # is_published = request.env['ir.config_parameter'].sudo().get_param('wamy_educational.is_published')
        # qcontext.update({
        #     'is_published': is_published})
        # return qcontext
    
    # def website_publish_button(self):
    #     self.ensure_one()
    #     return self.write({'website_published': not self.website_published})
    #

    
    