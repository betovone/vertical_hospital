# -*- coding: utf-8 -*-
{
    'name': "vertical_hospital",
    'summary': "Aplicación de prueba para Quilsoft",
    'description': "Test de programación",
    'author': "Marcelo Schiavone",
    'website': "",
    'category': 'Health',
    'version': '0.1',
    'depends': ['base', 'mail',],
    'data': [
        #'security/ir.model.access.csv',
        'sequences/vertical_hospital_sequence.xml',
        'views/views.xml',
        'views/vertical_hospital_tratamiento_view.xml',
        'views/vertical_hospital_paciente_view.xml',
        'views/vertical_hospital_menu.xml',
        'views/vertical_hospital_paciente_template.xml',
        'reports/vertical_hospital_report.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': 'register_routes',
}

