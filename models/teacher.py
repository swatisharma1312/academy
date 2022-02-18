# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class AcademyTeacher(models.Model):
    _name = 'academy.teacher'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Academy Teacher'

    course_ids = fields.One2many('academy.management', 'course', string='Course Name')
    name = fields.Char(string="course name")
    teacher_name = fields.Char(string="teacher name")





