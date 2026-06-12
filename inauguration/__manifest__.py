# -*- coding: utf-8 -*-
{
    'name': 'Inauguration',
    'version': '19.0.1.0.0',
    'summary': 'Marquer les contacts importants',
    'description': """
        Ce module ajoute une coche "Personne importante" sur la fiche contact,
        permettant d'identifier rapidement les personnes clés.
    """,
    'category': 'Contacts',
    'author': 'Auneor Conseil',
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
