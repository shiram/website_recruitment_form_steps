# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteRecruitmentFormSteps(http.Controller):
#     @http.route('/website_recruitment_form_steps/website_recruitment_form_steps/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_recruitment_form_steps/website_recruitment_form_steps/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_recruitment_form_steps.listing', {
#             'root': '/website_recruitment_form_steps/website_recruitment_form_steps',
#             'objects': http.request.env['website_recruitment_form_steps.website_recruitment_form_steps'].search([]),
#         })

#     @http.route('/website_recruitment_form_steps/website_recruitment_form_steps/objects/<model("website_recruitment_form_steps.website_recruitment_form_steps"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_recruitment_form_steps.object', {
#             'object': obj
#         })