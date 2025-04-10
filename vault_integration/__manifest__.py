# -*- coding: utf-8 -*-
{
    'name': "Secrets Vault Integration",
    'summary': """Securely manage secrets using HashiCorp Vault.""",
    'version': '18.0.1.0.0',
    'author': 'Harrison Consulting',
    'website': 'https://www.harrison.consulting',
    'sequence': 0,
    'license': 'GPL-3',
    'category': 'Tools',
    'depends': ['base','mail'],
    'data': [
        "security/ir.model.access.csv",
        'views/vault_secret_views.xml',
        'views/res_config_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}