# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.addons.http_routing.models.ir_http import slug
from odoo.http import request
from werkzeug.exceptions import NotFound

@http.route('''/jobs/apply/<model("hr.job", "[('website_id', 'in', (False, current_website_id))]"):job>''', type='http', auth="public", website=True)
def jobs_apply(self, job, **kwargs):
	if not job.can_access_from_current_website():
		raise NotFound()

	countries = self.env['res.country'].search([])
	print(countries)

	error = {}
	default = {}
	if 'website_hr_recruitment_error' in request.session:
		error = request.session.pop('website_hr_recruitment_error')
		default = request.session.pop('website_hr_recruitment_default')
	return request.render("website_recruitment_form_steps.website_hr_recruitment_apply", {
		'job': job,
		'error': error,
		'default': default,
		'countries': countries,
	})