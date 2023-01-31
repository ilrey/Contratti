from dataclasses import field
from email.policy import default
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class ContrattiContratto(models.Model):
    _name = "contratti.contratto"
    _description = "Contratto"

    #region Default
    Con_CognomeClienteContratto = fields.Char(string='Cognome')
    Con_NomeCliente = fields.Char(string='Nome')
    Con_CodFiscaleCliente = fields.Char(string='Codice Fiscale')
    Con_TipoDocumento = fields.Selection([('CARTA_IDENTITA','CARTA IDENTITA'), ('PATENTE', 'PATENTE'), ('PASSAPORTO', 'PASSAPORTO')])   
    Con_Numero = fields.Char(string='Numero')
    Con_RilasciatoDa = fields.Selection([('COMUNE','COMUNE'), ('MCTC', 'MCTC'), ('UCO', 'UCO'), ('QUESTURA','QUESTURA')])   
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
    Con_Documento = fields.Binary(string='Documento cliente')
    Con_Documento_Name = fields.Char(string="File name")
    #endregion 
    
    Con_Telefonia = fields.Boolean(string="Telefonia", default=False)
    Con_Pod_bool = fields.Boolean(string="Luce", default=False)
    Con_Pdr_bool = fields.Boolean(string="Gas", default=False)
    Con_Fotov_bool = fields.Boolean(string="Fotovoltaico", default=False)
    Con_Auto_bool = fields.Boolean(string="Noleggio Auto", default=False)


    #region Telefonia 
    Con_GestoreAttuale = fields.Selection([('NUOVA','NUOVA ATTIVAZIONE'), ('TIM', 'TIM'), ('VODAFONE', 'VODAFONE'), ('WINDTRE', 'WIND TRE'), 
                                           ('ILIAD_ITALIA', 'ILIAD ITALIA'), ('FASTWEB', 'FASTWEB'), ('COOPVOCE', 'COOPVOCE'), ('HO', 'HO.'), 
                                           ('KENA', 'KENA MOBILE'), ('LYCAMOBILE', 'LYCAMOBILE'), ('POSTEMOBILE', 'POSTEMOBILE'), ('RABONAMOBILE', 'RABONA MOBILE'), 
                                           ('TISCALI', 'TISCALI'), ('ILLIAD', 'ILLIAD')])
    Con_Tel_MetodoPagamento = fields.Selection([('IBAN','IBAN'), ('CC', 'CC')])
    Con_OffertaAttuale = fields.Char(string='Offerta Attuale:')
    Con_CodMigrazione = fields.Char(string='Codice Migrazione:')
    Con_Num_Migrare = fields.Char(string='Numero da Migrare:')
    Con_Num_Sim = fields.Char(string='Numero SIM:')
    Con_Tel_Documento = fields.Binary(string='Documento telefonia')
    #endregion

    #region Energia    
    Con_Pod = fields.Char(string='POD:')
    Con_Pod_MetodoPagamento = fields.Selection([('IBAN','IBAN'), ('BOLLETTINO', 'BOLLETTINO'), ('FINANZIAMENTO', 'FINANZIAMENTO')])
    Con_Pod_AttSocVendita = fields.Char(string="Attuale societa' vendita:")
    Con_Pod_Potenzakvw = fields.Char(string='Potenza KW:')
    Con_Pod_ConsAnnuo= fields.Char(string='Consumo annuo:')
    Con_Pod_Documento = fields.Binary(string='Documento Energia')
    #Con_Pod_DataAttivazione= fields.Date(string='Data attivazione:')

     
    Con_Pdr = fields.Char(string='PDR:')
    Con_Pdr_AttSocVendita = fields.Char(string="Attuale societa' vendita:")   
    Con_Pdr_ConsAnnuo= fields.Char(string='Consumo annuo:')
    Con_Pdr_PotenzaSMC = fields.Char(string='Potenza Standard Metro Cubo:')
    #endregion


    #region Fotovoltaico
    Con_Fotov_MetodoPagamento = fields.Selection([('UNICATRANCHE', 'BONIFICO UNICA TRANCHE'), ('MULTITRANCHE', 'BONIFICO MULTI TRANCHE'), ('FINANZIAMENTO','FINANZIAMENTO')])
    Con_Fotov_Wallbox = fields.Boolean(string="Wallbox", default=False)
    Con_Fotov_PotenzaImp = fields.Char(string='Potenza impianto:')
    Con_Fotov_Potenzabatt = fields.Char(string='Potenza batteria accumolo:')
    Con_Fotov_Pompa = fields.Char(string='Pompa di calore:')
    #enregion

    #region NoleggioAuto
    Con_Auto_AutoVenduta = fields.Char(string='Auto venduta:')
    Con_Fotov_DurataNoleggio = fields.Char(string='Durata noleggio:')
    #enregion


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

    @api.model
    def create(self, vals):
        for i in list(vals):
            if type(vals[i])!=bool and type(vals[i])!=int:               
                vals[i] = vals[i].upper()
        return super(ContrattiContratto, self).create(vals)

    def write(self, vals):
        for i in list(vals):
            if type(vals[i])!=bool and type(vals[i])!=int:               
                vals[i] = vals[i].upper()
        return super(ContrattiContratto, self).write(vals)

    #def buttone_prova(self):       
    #    delta = self.env['dms.file'].write({'name' : 'provafie'})
    #    return delta













    #calendar_module
    #def map_url(self):
    #    url_string = ("https://www.google.com/maps/dir//+{},+{},+{}".format(self.x_indirizzo, self.x_civico, self.x_citta))
    #    if False in (self.x_indirizzo, self.x_civico, self.x_citta):
    #        raise ValidationError(_("Indirizzo non completo"))
    #    else:
    #        return{      
    #            'type': 'ir.actions.act_url',
    #            'url': url_string
    #            }
    