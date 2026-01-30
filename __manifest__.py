{
    'name': 'Alquiler de productos',
    'version': '1.0',
    'summary': 'Módulo para gestionar el alquiler de productos',
    'category': 'Custom',
    'author': 'Pablo García',
    'website': 'https://tuweb.com',
    'license': 'LGPL-3',
    'depends': ['base', 'product', 'sale'],
    'icon': '/alquiler_producto/static/description/icon57.png',
    'data': [
        'data/alquiler_cron.xml',
        'views/alquiler_producto_views.xml',
        'security/ir.model.access.csv',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'description': """
Módulo de Odoo para la gestión de alquileres de productos de la empresa ElectroWord.
Permite asignar clientes y productos disponibles, calcular automáticamente
la fecha de finalización del préstamo y gestionar el estado del alquiler
mediante tareas programadas (cron jobs).
"""
}