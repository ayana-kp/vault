# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    vault_enabled = fields.Boolean(string='Allow users to use Vault', config_parameter='vault_integration.vault_enabled')
    vault_url = fields.Char(string='Vault URL',config_parameter='vault_integration.vault_url',
                            help="The URL of your Vault instance (e.g., https://vault.example.com:8200).",
                            )
    vault_token = fields.Char(string='Vault Token',config_parameter='vault_integration.vault_token',
                              help="Your Vault access token.  Consider using AppRole for better security.")

