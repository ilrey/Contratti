from dataclasses import field
from email.policy import default
from odoo import api, fields, models

class ContrattiContratto(models.Model):
    _name = "contratti.contratto"
    _description = "Contratto"

    Con_CognomeClienteContratto = fields.Char(string='Cognome')
    Con_NomeCliente = fields.Char(string='Nome')
    Con_CodFiscaleCliente = fields.Char(string='Codice Fiscale')
    Con_TipoDocumento = fields.Selection([('Carta_identita','Carta identita'), ('patente', 'Patente'), ('passaporto', 'Passaporto')])
    Active = fields.Boolean(string="Active", default=True)