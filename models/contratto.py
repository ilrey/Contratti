from dataclasses import field
from email.policy import default
from odoo import api, fields, models

class ContrattiContratto(models.Model):
    _name = "contratti.contratto"
    _description = "Contratto"

    #region Default
    Con_CognomeClienteContratto = fields.Char(string='Cognome')
    Con_NomeCliente = fields.Char(string='Nome')
    Con_CodFiscaleCliente = fields.Char(string='Codice Fiscale')

    Con_TipoDocumento = fields.Selection([('Carta_identita','Carta identita'), ('patente', 'Patente'), ('passaporto', 'Passaporto')])   
    Con_Numero = fields.Char(string='Numero')
    Con_RilasciatoDa = fields.Selection([('comune','Comune'), ('mctc', 'MCTC'), ('uco', 'UCO'), ('questura','Questura')])   
    Con_DataRilascio = fields.Date(string='Data rilascio')

    Con_Telefono = fields.Char(string='Telefono')
    Con_Cellulare = fields.Char(string='Cellulare')
    Con_Email = fields.Char(string='Email')
    Con_Pec = fields.Char(string='PEC')
    Con_MetodoPagamento = fields.Selection([('iban','Iban'), ('bollettino', 'Bollettino'), ('finanziamento', 'Finanziamento')])   
     
    Con_Indirizzo = fields.Char(string='Indirizzo')
    Con_Civico = fields.Char(string='N.Civico')
    Con_Scala = fields.Char(string='Scala')
    Con_Interno = fields.Char(string='Interno')
    Con_Citta = fields.Char(string="Citta'")

    Con_Note = fields.Html('Note')
    #endregion 

    #region Telefonia
    Con_Telefonia = fields.Boolean(string="Telefonia", default=False)
    Con_GestoreAttuale = fields.Selection([('nuoca','Nuova Attivazione'), ('vuoto1', 'vuoto'), ('vuoto2', 'vuoto2')])
    Con_OffertaAttuale = fields.Char(string='Offerta Attuale:')
    Con_CodMigrazione = fields.Char(string='Codice Migrazione:')
    Con_TelefoniAttivati = fields.Char(string='Telefoni Attivati:')
    Con_LineeAttive = fields.Char(string='N. Linee Attive:')
    #endregion

    #region Energia
    Con_Pod_bool = fields.Boolean(string="Luce", default=False)
    Con_Pdr_bool = fields.Boolean(string="Gas", default=False)

    Con_Pod = fields.Char(string='POD:')
    Con_Pod_ProvMervato = fields.Boolean(string="Provenienza mercato libero", default=False)
    Con_Pod_AttSocVendita = fields.Char(string="Attuale societa' vendita:")
    Con_Pod_Potenzakvw = fields.Char(string='Potenza KW:')
    Con_Pod_Distributore = fields.Char(string='Distributore di zona:')
    Con_Pod_ConsAnnuo= fields.Char(string='Consumo annuo:')
    Con_Pod_DataAttivazione= fields.Date(string='Data attivazione:')
    Con_Pod_AttDis = fields.Selection([('pod_attivo','Attivo'), ('pod_disattivo', 'Disattivo')])

    Con_Pdr = fields.Char(string='PDR:')
    Con_Pdr_AttSocVendita = fields.Char(string="Attuale societa' vendita:")
    Con_Pdr_Distributore = fields.Char(string='Distributore di zona:')
    Con_Pdr_ConsAnnuo= fields.Char(string='Consumo annuo:')
    Con_Pdr_DataAttivazione= fields.Date(string='Data attivazione:')
    Con_Pdr_Riscaldamento = fields.Boolean(string="Riscaldamento", default=False)
    Con_Pdr_CottAcqua = fields.Boolean(string="Cottura e/o acqua", default=False)
    Con_Pdr_AttDis = fields.Selection([('pod_attivo','Attivo'), ('pod_disattivo', 'Disattivo')])
    #endregion

    active = fields.Boolean(string="Active", default=True)
    user_id = fields.Many2one('res.users', string='Responsible', tracking=True,  default=lambda self: self.env.user)


    def open_file_upload(self):
        return{
            'res_model': 'dms.file',
            #'res_id': 12,
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': self.env.ref('dms.view_dms_file_form').id,
            }
    