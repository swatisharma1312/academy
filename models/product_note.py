# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ProductNote(models.Model):
    _name = 'product.note'
    _description = 'Product Note'

    details = fields.Char(string='Product Details')
    product_id = fields.Many2one('product.data', string="Product id")



