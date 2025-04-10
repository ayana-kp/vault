# -*- coding: utf-8 -*-

from odoo import models, fields
import requests


class VaultSecret(models.Model):
    _name = 'vault.secret'
    _description = 'Secret stored in HashiCorp Vault'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Secret Name', required=True, tracking=True)
    vault_path = fields.Char(string='Vault Path', required=True,
                             help="The path to the secret in Vault (e.g., secret/data/mysecret).",
                             tracking=True)
    vault_data = fields.Text(string='Secret Data',
                             help="The actual secret data")
    last_retrieved = fields.Datetime(string='Last Retrieved', tracking=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('connected', 'Connected'),
        ('connection_failed', 'Connection Failed')
    ], string='Connection Status', default='draft', tracking=True)

    def action_test_connection(self):
        """Retrieves the secret data from Vault."""
        vault_is_active = self.env['ir.config_parameter'].sudo().get_param(
            'vault_integration.vault_enabled')

        if self.vault_path and vault_is_active:
            vault_url = self.env['ir.config_parameter'].sudo().get_param(
                'vault_integration.vault_url')
            token = self.env['ir.config_parameter'].sudo().get_param(
                'vault_integration.vault_token')
            if not vault_url or not token:
                raise ValueError(
                    "Vault URL or token is missing in system parameters.")
            headers = {
                "X-Vault-Token": token,
                "Content-Type": "application/json"
            }
            secret_path = f"v1/{self.vault_path}"  # Adjust path if using KV engine v2
            request_url = f"{vault_url}/{secret_path}"
            try:
                response = requests.get(request_url, headers=headers,
                                        timeout=10)
                response.raise_for_status()
                secret_data = response.json().get('data', {})
                print('secret_data', secret_data)
                self.status = 'connected'
                return secret_data
            except requests.exceptions.RequestException as e:
                self.status = 'connection_failed'
                raise ValueError(f"Failed to fetch secret from Vault: {str(e)}")
        else:
            self.status = 'connection_failed'
            raise ValueError("Vault path is missing or Vault is not enabled.")
