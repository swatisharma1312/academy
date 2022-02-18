# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProductData(models.Model):
    _name = 'product.data'
    _description = 'Product Data'

    name = fields.Char(string='Product Name')
    p_category = fields.Many2one('product.category', string="Product Category")
    category = fields.Many2one('product.public.category', string="Ecommerce Category")
    p_price = fields.Float(string="Product Price")
    description = fields.Char(string="Short Description")
    state = fields.Selection([('draft', 'Draft'),
                              ('product_created', 'Product Created')
                              ], default='draft', string="Status",)
    publish = fields.Boolean(string="Publish Product")
    note_ids = fields.One2many('product.note', 'product_id', string="Note")
    product_id = fields.Many2one('product.template', string="Product id")
    sku = fields.Char(string="Internal Refernce")

    def button_create(self):
        check_record = self.env['product.template'].search([('default_code', '=', self.sku)], limit=1)
        if len(check_record) >= 1:
            self.write({'product_id': check_record.id })

        else:
            create_record = self.env['product.template'].create({
                                             'name': self.name,
                                             'description': self.description,
                                             'categ_id': self.p_category.id,
                                             'standard_price': self.p_price})
            self.write({'product_id': create_record.id })
        self.state = 'product_created'

    def button_publish(self):
        if self.product_id:
            if self.product_id.is_published != True:
                self.product_id.is_published = True
                self.publish = True

        else:
            raise ValidationError("No Related button,Please Create first")

    @api.constrains('sku')
    def check_sku(self):
        all_data = self.env['product.data'].search([])
        for rec in all_data:
            if rec.sku == self.sku and rec.id != self.id:
               raise ValidationError("There is similar")
               









