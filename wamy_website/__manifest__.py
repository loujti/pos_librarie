# Copyright 2014-2016 Barroux Abbey (http://www.barroux.org)
# Copyright 2014-2016 Akretion France
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Wamy Website',
    'version': '14.0.1.0.0',
    'category': 'website',
    'summary': 'Wamy website',
    'author': 'ATIT',
    'website': '',
    'depends': ['base', 'website',
                'website_sale',
                'website_partner',
                'contacts',
                ],
    'data': [
        
        # View
        # 'view/assets.xml',
        
        
        
        
        'security/ir.model.access.csv',
        'data/website_menu_data.xml',
        # Views
        'views/website_slider.xml',
        'views/wamy_statistics.xml',
        'view/website_homepage.xml',
        'view/students_scholarship.xml',
        
    ],

    'demo': [
    ],
    'assets': {
        'web.assets_frontend': [
            'wamy_website/static/src/css/style.css',
            'wamy_website/static/src/js/validation_email.js']},


    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,

}
