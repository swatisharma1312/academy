# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class AcademyManagement(models.Model):
    _name = 'academy.management'
    _description = 'Academy Management'

    name = fields.Char(string='Student Name')
    biography = fields.Char()
    course = fields.Many2one('academy.teacher', string="Cousre Name")



