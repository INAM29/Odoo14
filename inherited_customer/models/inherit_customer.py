# -*- coding: utf-8 -*-
from odoo import fields, models

class InheritCustomer(models.Model):
    _inherit = 'res.partner'

    description = fields.Text(string='Description')