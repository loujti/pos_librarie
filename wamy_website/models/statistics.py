from odoo import api, fields, models, http
from odoo.tools import safe_eval

from odoo.addons.website.controllers.main import Website


class WamyStatistics(models.Model):
    _name = 'wamy.website.statistics'
    _description = 'Wamy Website Statistics'

    name = fields.Char('Name', required=True)
    title = fields.Char('Title',translate=True, required=True)
    icon = fields.Char('Icon', help="Font awesome icon e.g. fa-tasks")
    model_name = fields.Char('Model Name')
    total_count = fields.Integer(compute='compute_total_count')
    circle_background_color = fields.Char('Color of Circle')

    model_id = fields.Many2one('ir.model', 'Model', ondelete='set default', required=True)
    filter_domain = fields.Char(string='Apply on', help="If present, this condition must be satisfied before executing the action rule.")

    @api.onchange('model_id')
    def onchange_model_id(self):
            self.model_name = self.model_id.model

    @api.depends('model_name', 'filter_domain')
    def compute_total_count(self):
        for rec in self:
            if rec.model_name and rec.filter_domain:
                domain = []
                context = dict(self._context)
                if rec.filter_domain:
                    domain = safe_eval.safe_eval(rec.filter_domain)
                print('filter_domain', domain)
                records = self.env[rec.model_name].with_context(context).search(domain)

                print('records',records)
                rec.total_count = len(records.ids)
            else:
                rec.total_count = 0

