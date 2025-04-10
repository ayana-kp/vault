# -*- coding: utf-8 -*-
import json
import requests
from odoo import fields, models
from odoo.exceptions import ValidationError


class ProductCategory(models.Model):
    """Inherits product_category for including Pipedrive fields and functions"""
    _inherit = 'product.category'

    pipedrive_reference = fields.Char(string='Pipedrive Reference',
                                      help="Pipedrive Id of the Partner")

    def write(self, vals):
        """Inherited to update product field in pipedrive"""
        data = {}
        pipedrive_categ = self.env['pipedrive.record'].sudo().search(
            [('record_type', '=', 'categ'), ('odoo_ref', '=', self.id)])
        if 'name' in vals.keys() and pipedrive_categ:
            data['label'] = vals['name']
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            response = requests.put(
                url=f'https://api.pipedrive.com/v1/productFields/'
                    f'{self.pipedrive_reference}',
                params={
                    'api_token': self.env.user.company_id.api_key,
                }, timeout=10, headers=headers, data=json.dumps(data))
            if 'error' in response.json().keys():
                raise ValidationError(
                    response.json()['error'])
        return super().write(vals)

    def unlink(self):
        """Inherited to delete the product field from Pipedrive"""
        pipedrive_categ = self.env['pipedrive.record'].sudo().search(
            [('record_type', '=', 'categ'), ('odoo_ref', '=', self.id)])
        if pipedrive_categ:
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            response = requests.delete(
                url=f'https://api.pipedrive.com/v1/productFields/'
                    f'{self.pipedrive_reference}',
                params={
                    'api_token': self.env.user.company_id.api_key,
                }, timeout=10, headers=headers)
            if 'error' in response.json().keys():
                raise ValidationError(
                    response.json()['error'])
        return super().unlink()
