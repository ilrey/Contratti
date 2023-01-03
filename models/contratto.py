from dataclasses import field
from email.policy import default
from odoo import api, fields, models

class ContrattiContratto(models.Model):
    _name = "contratti.contratto"
    _description = "Contratto"

    Con_CognomeClienteContratto = fields.Char(string='Cognome')
    Con_NomeCliente = fields.Char(string='Nome')
    Con_CodFiscaleCliente = fields.Char(string='Codice Fiscale')
    active = fields.Boolean(string="Active", default=True)
    Con_TipoDocumento = fields.Selection([('Carta_identita','Carta identita'), ('patente', 'Patente'), ('passaporto', 'Passaporto')])
    user_id = fields.Many2one('res.users', string='Agente', tracking=True,  default=lambda self: self.env.user)