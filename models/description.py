# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class AcademyManagement(models.Model):
    _inherit = 'product.template'

    description = fields.Char(string='Description')




