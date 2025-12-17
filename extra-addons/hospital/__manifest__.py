# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': "Módulo que permita gestionar pacientes y médicos de un hospital",

    'description': """
Para cada paciente, tendremos un modelo con los siguientes datos:
● Nombre y apellidos del paciente.
● Síntomas.

Para cada médico, tendremos un modelo con los siguientes datos:
● Nombre y apellidos del médico.
● Número de colegiado.

Por cada vez que un médico ha atendido a un paciente, tendremos un modelo indicando el diagnóstico.
Un paciente puede haber sido atendido por varios médicos y un médico puede haber atendido a varios pacientes.
    """,

    'author': "Jorge Durán Cruz",
    'website': "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.youtube.com/watch%3Fv%3DdQw4w9WgXcQ&ved=2ahUKEwjKh7KD-5SRAxUJ1wIHHRrAEP4QwqsBegQIEhAB&usg=AOvVaw0aHtehaphMhOCAkCydRLZU",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        "views/diagnosticos_views.xml",
        "views/medicos_views.xml",
        "views/pacientes_views.xml",
        "views/menu.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

