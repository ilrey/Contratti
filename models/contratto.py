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
    Con_Numero = fields.Char(string='Numero')
    Con_RilasciatoDa = fields.Char(string='Rilasciato Da:')
    Con_DataRilascio = fields.Date(string='Data rilascio')

    Con_Telefono = fields.Char(string='Telefono')
    Con_Cellulare = fields.Char(string='Cellulare')
    Con_Email = fields.Char(string='Email')
    Con_Pec = fields.Char(string='PEC')
     
    Con_Indirizzo = fields.Char(string='Indirizzo')
    Con_Civico = fields.Char(string='N.Civico')
    Con_Scala = fields.Char(string='Scala')
    Con_Interno = fields.Char(string='Interno')
    Con_Citta = fields.Char(string="Citta'")

    Con_Note = fields.Html('Note')
    
    active = fields.Boolean(string="Active", default=True)
    user_id = fields.Many2one('res.users', string='Responsible', tracking=True,  default=lambda self: self.env.user)


    def open_file_upload(self):
        return{
            'res_model': 'dms.file',
            #'res_id': 12,
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': self.env.ref('dms.view_dms_file_form').id,
            'name': 'prova'
            }
            