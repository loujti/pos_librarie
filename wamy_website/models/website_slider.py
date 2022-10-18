from odoo import api, fields, models, http, _
from odoo.exceptions import ValidationError, RedirectWarning, Warning, UserError
import re
from odoo.addons.website.controllers.main import Website

class WebsiteSliders(models.Model):
    _name = 'wamy.website.sliders'
    _description = 'Wamy Website Slider'

    name = fields.Char('Name')
    image = fields.Image('Image')
    description = fields.Html('Description')
    url = fields.Char('URL Address')




    @api.constrains('url')
    def check(self):
        regex_url = re.compile(
        r'^(?:http|ftp)s?://' r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if self.url:
            if not (re.fullmatch(regex_url, self.url)):
                raise ValidationError(_('Invalid Url'))
            
            
       