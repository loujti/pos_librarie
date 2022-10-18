# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http, _
from odoo.http import request
from werkzeug.exceptions import NotFound
from odoo.exceptions import ValidationError, RedirectWarning, Warning, UserError
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
import logging

_logger = logging.getLogger(__name__)


class WebsiteSchoolarship(http.Controller):
    def sitemap_schoolarship(env, rule, qs):
        if not qs or qs.lower() in '/student_schoolarship':
            yield {'loc': '/student_schoolarship'}
    
    @http.route(['/student_schoolarship','/student_schoolarship/page/<int:page>'], type='http', auth="public", website=True,sitemap=sitemap_schoolarship, page=1 ,)
    def schoolarship(self, **kwargs):
        schoolarship_details_ids = request.env['educational.schoolarship.details'].sudo().search([('state', '=', 'progress')])
        pager = portal_pager(
                            url="/student_schoolarship",
                            total=len(schoolarship_details_ids),
                            )
        return request.render("wamy_website.schoolarship", {
            'schoolarship_educational': schoolarship_details_ids,
            
            'pager': pager,
    
        })
        
    def publish(self, id, object):
        Model = request.env[object]
        record = Model.browse(int(id))

        values = {}
        if 'website_published' in Model._fields:
            values['website_published'] = not record.website_published
            record.write(values)
            return bool(record.website_published)
        return False   
        
        
        
    @http.route('''/student_schoolarship/detail/<model("educational.schoolarship.details"):schoolarship>''', type='http', auth="public", website=True, sitemap=True)
    def Schoolarship_detail(self, schoolarship, **kwargs):
        if not schoolarship.can_access_from_current_website():
            raise NotFound()
        return request.render("wamy_website.detail", {
            'schoolarship': schoolarship,
        })
        
    @http.route('''/schoolarship/conditions/<model("educational.schoolarship.details"):schoolarship>''', type='http', auth="public", website=True, sitemap=True)
    def schoolarship_conditions(self, schoolarship, **kwargs):
        if not schoolarship.can_access_from_current_website():
            raise NotFound()
        return request.render("wamy_website.conditions", {
        'schoolarship': schoolarship,
      
           
        })
        
        
    @http.route('''/schoolarship/apply/<model("educational.schoolarship.details"):schoolarship>''', type='http', auth="public", website=True, sitemap=True)
    def schoolarship_apply(self, schoolarship, **kwargs):
        if not schoolarship._get_validate_schoolarship():
            return request.render("wamy_website.conditions", {'schoolarship': schoolarship,
                                                             'error': _('You cannot apply for this scholarship, The last date for registration has expired!')})
        country_ids= request.env['res.country'].sudo().search([])
        return request.render("wamy_website.aplly", {
        'schoolarship': schoolarship,
        'country_ids': country_ids,
       'scholarship_id':schoolarship,
           
        }) 
        
        
        
    @http.route(['/create/student_schoolarship'], type='http', auth="public", website=True, csrf=False , sitemap=True)
    def create_student_schoolarship(self, **kw):
        scholarship_id= kw.get('scholarship_id')
        scholarship_id = int(scholarship_id) if scholarship_id else False
        try:
            values = {
                'name': kw.get('name'),
                'phone': kw.get('phone'),
                'email': kw.get('email'),
               'notes': kw.get('notes'),
               'is_student': True,
               'social_situation': kw.get('social_situation'),
            }
            partner_id = request.env['wamy.beneficiaire'].sudo().create(values)
            schoolarship_request_vals={
                 'partner_id':partner_id.id,
                 'scholarship_id': scholarship_id,
                 
                   }
            
            request.env['educational.schoolarship.request'].sudo().create(schoolarship_request_vals)
            msg=_("Your request has been sent now")
        except Exception as e:
            _logger.info("New schoolarship Wamy error: %s", e)
            msg=_("Some Thing Wrong!")
        return request.render("wamy_educational_portal.response_create_episode",{'msg':msg})
  
        
        