# -*- coding: utf-8 -*-
{
    'name': "Odoo Pipedrive Connector",
    'version': '18.0.1.0.0',
    'category': 'Productivity',
    'summary': """Integrate contacts, products and leads between Pipedrive 
     and Odoo""",
    'description': """This module helps to successfully import all products, 
     contacts and leads between Pipedrive to Odoo. Also, it is possible to 
     export all these data from Odoo to Pipedrive. All import and export 
     operations can be performed in a single button click.""",
    'depends': ['account', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_company_views.xml',
        'views/product_template_views.xml',
        'views/crm_lead_views.xml',
        'views/product_category_views.xml',
        'views/res_partner_views.xml'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
