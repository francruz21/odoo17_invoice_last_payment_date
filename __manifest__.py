{
    'name': 'Fecha Último Pago en Facturas',
    'version': '1.0',
    'summary': 'Añade campo de fecha del último pago en facturas',
    'description': """
        Muestra la fecha del último pago registrado para cada factura.
    """,
    'author': 'Francisco Cruz',
    'website': 'https://www.linkedin.com/in/francisco-cruz-1b918b27b/',
    'depends': ['account'],
    'data': [
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
}
