from odoo import http
from odoo.http import request

class Academy(http.Controller):



    @http.route('/academy/student/', auth="public")
    def index(self, **kw):
        # return "hello swati world"
        students = request.env['academy.management'].sudo().search([])
        return http.request.render('academy.index', {
            'students': students
         })

    @http.route('/academy/<model("academy.management"):student>', auth="public", website=True)
    def student(self, student):
        # return "hello swati world"
        # students = request.env['academy.management'].sudo().search([])
        return http.request.render('academy.biography', {
            'person': student
        })



