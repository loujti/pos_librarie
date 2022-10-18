from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.web import Home


class WamyWebsite(Home):

    @http.route(['/'], type='http', auth="public", website=True, sitemap=True)
    def index(self, **kw):
        super(WamyWebsite, self).index()
        sliders_details = request.env['wamy.website.sliders'].sudo().search([])
        partners = request.env['res.partner'].sudo().search([('website_published', '=', True)])

        return request.render("wamy_website.wamy_slider_homepage", {'my_sliders': sliders_details,
                                                                    'my_partners': partners,
                                                                    })
