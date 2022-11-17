# -*- coding: utf-8 -*-
{
    'name': "expense_reconcile",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources/Depenses',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': ['expense_request'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/account_bank_statement_views.xml',
        'views/expense_line_reconcile_views.xml',
        'views/bank_statement_reconcile_views.xml',
        'views/expense_request_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}
