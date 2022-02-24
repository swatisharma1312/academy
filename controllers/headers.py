from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo import http
from odoo.http import request
from odoo import registry as registry_get
import json
import logging
_logger = logging.getLogger(__name__)


class Header(http.Controller):

    @http.route('/api/product_template/new_create', csrf=False, type='http', auth='none', methods=['POST'])
    def cert_auth(self, **kwargs):
        response = {}
        request_data = request.httprequest.data and json.loads(request.httprequest.data.decode('utf-8')) or {}
        print("I am in request", request_data)
        product_name = request_data.get("name")
        product_category = request_data.get("category")
        print("I access product", product_name)
        print("I access product", product_category)
        db_name = tools.config['db_name']
        context = {}
        registry = registry_get(db_name)
        with registry.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, context)
            try:

                name = request_data.get("name")
                price = request_data.get("price")
                description = request_data.get("description")
                category_id = request_data.get("categ_id")
                sku = request_data.get("sku")
                print("i m name", name)
                print("i m price", price)
                print("i m description", description)
                print("im name", sku)

                student_obj = env['product.data'].sudo().create({
                    "name": name,
                    "p_price": price,
                    "description": description,
                    "p_category": category_id,
                    "sku": sku
                })
                print("i am in student", student_obj)
                response.update({"status": 200,
                         "product_id" : student_obj.id,
                         "error_msg": False})

            except Exception as e:
                _logger.info("e::::::::::::::::%s", e, exc_info=True)
                response.update({
                 "status": 500,
                 "auth": False,
                 "error_msg": str(e)
                  })

        return json.dumps(response)

    @http.route('/api/product_template/create_upadte', csrf=False, type='http', auth='none', methods=['POST'])
    def search_auth(self, **kwargs):
        response = {}
        request_data = request.httprequest.data and json.loads(request.httprequest.data.decode('utf-8')) or {}
        print("I am in request", request_data)
        id = request_data.get("product_id")
        print("I am in request", id)
        db_name = tools.config['db_name']
        context = {}
        registry = registry_get(db_name)
        with registry.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, context)
            student_obj = env['product.data'].sudo().search([('id', '=', id)])
            print(student_obj)
            student_obj.button_create()

            response.update({"status": 200,
                         "product_temp_id": student_obj.product_id.id,
                         "error_msg": False})

        return json.dumps(response)

    @http.route('/api/product_data/update', csrf=False, type='http', auth='none', methods=['POST'])
    def update_auth(self, **kwargs):
        response = {}
        request_data = request.httprequest.data and json.loads(request.httprequest.data.decode('utf-8')) or {}
        print("I am in request", request_data)
        id = request_data.get("product_id")
        data = request_data.get("data")
        print("I am in request", id)
        print("I am in request", data)
        db_name = tools.config['db_name']
        context = {}
        registry = registry_get(db_name)
        with registry.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, context)
            student_obj = env['product.data'].sudo().search([('id', '=', id)])
            if student_obj:
                student_obj.write({"name": data["name"], "sku": data["sku"]})
            else:
                response.update({"error_msg": "Product Data is not exist"})




            response.update({"status": 200,
                             "product_temp_id": student_obj.product_id.id,
                             "error_msg": False})

        return json.dumps(response)








