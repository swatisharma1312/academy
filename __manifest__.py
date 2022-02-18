{
    'name': "Academy Management",

    'category': 'Sales/Sales',

    'sequence': 5,

    'summary': "academy Management",

    'description': """Academy Management""",

    'author': "Swati Sharma",

    'version': '1.0',

    'depends': ['base', 'mail', 'sale', 'purchase', 'account', 'product', 'point_of_sale', 'website', ],

    'data': ['security/ir.model.access.csv',
             'views/academy.xml',
             'views/academy_temp.xml',
             'views/teacher.xml',
             'views/description.xml',
             'views/ecommerce_product.xml',
             'views/products.xml',
             'views/product_data.xml'],
    'qweb': [],
    'installable': True,

    'application': True,
}