# -*- coding: utf-8 -*-
from odoo import fields, models


class PipedriveRecord(models.Model):
    """Model to hold the Pipedrive Records"""
    _name = 'pipedrive.record'
    _description = 'Pipedrive Record'
    _rec_name = 'pipedrive_reference'

    pipedrive_reference = fields.Char(string='Pipedrive Id',
                                      help="Pipedrive reference of the record")
    record_type = fields.Selection(
        [('product', 'Product'), ('lead', 'Lead'), ('partner', 'Partner'), ('categ', 'Category')],
        string='Type',
        help='Type of record')
    odoo_ref = fields.Integer(string='Odoo Reference',
                              help="Odoo reference of the record")
