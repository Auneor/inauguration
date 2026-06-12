# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_important = fields.Boolean(
        string='Personne importante',
        default=False,
        help='Cochez cette case pour marquer ce contact comme une personne importante.',
    )
