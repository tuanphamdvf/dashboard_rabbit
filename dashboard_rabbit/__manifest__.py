# -*- coding: utf-8 -*-
{
    'name': "Dashboard Rabbit v2",
    "summary": "The dashboard includes a revenue chart, a profit chart, an order count chart, a product-wise revenue chart",
    'description': """The dashboard includes a revenue chart, a profit chart, an order count chart, a product-wise revenue chart, an employee-wise revenue chart, total revenue, cash revenue, bank transfer revenue, purchasing expenses, and visually complete customer statistics.
    """,
    "price": "20",
    "currency": "EUR",
    'license': 'GPL-3',
    'author': "TTN SOFTWARE",
    'website': "TTNSOFTWARE.STORE",
    'category': 'App',
    'version': '15.2.1',
    'depends': ['base', 'mrp', 'sale', 'pos_sale', "hr", "purchase"],

    'data': [
        'security/ir.model.access.csv',
        'views/owl_templates/owl_customer.xml',
        'views/views.xml',
        'views/templates.xml',


    ],
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_qweb': [
            'dashboard_rabbit/static/src/xml/*',
            'dashboard_rabbit/static/src/xml/owl/*',
        ],
        'web.assets_backend': [
            'dashboard_rabbit/static/src/components/**/*',
            'dashboard_rabbit/static/src/scss/**/*',
            'dashboard_rabbit/static/lib/*',
            'dashboard_rabbit/static/src/js/**/*',
            'dashboard_rabbit/static/src/js/*',
        ],

    },

    'images': ['static/img/main_screenshot.gif']
}
