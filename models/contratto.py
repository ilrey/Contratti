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
    Con_TipoDocumento = fields.Selection([('Carta_identita','Carta identita'), ('patente', 'Patente'), ('passaporto', 'Passaporto')])   
    Con_Numero = fields.Char(string='Numero')
    Con_RilasciatoDa = fields.Selection([('comune','Comune'), ('mctc', 'MCTC'), ('uco', 'UCO'), ('questura','Questura')])   
    Con_DataRilascio = fields.Date(string='Data rilascio')
    Con_Telefono = fields.Char(string='Telefono')
    Con_Cellulare = fields.Char(string='Cellulare')
    Con_Email = fields.Char(string='Email')
    Con_Pec = fields.Char(string='PEC')
    #Con_MetodoPagamento = fields.Selection([('iban','Iban'), ('bollettino', 'Bollettino'), ('finanziamento', 'Finanziamento')])      
    Con_Indirizzo = fields.Char(string='Indirizzo')
    Con_Civico = fields.Char(string='N.Civico')
    Con_Scala = fields.Char(string='Scala')
    Con_Interno = fields.Char(string='Interno')
    Con_Citta = fields.Char(string="Citta'")
    Con_Note = fields.Html('Note')
    #endregion 
    
    Con_Telefonia = fields.Boolean(string="Telefonia", default=False)
    Con_Pod_bool = fields.Boolean(string="Luce", default=False)
    Con_Pdr_bool = fields.Boolean(string="Gas", default=False)
    Con_Fotov_bool = fields.Boolean(string="Fotovoltaico", default=False)
    Con_Auto_bool = fields.Boolean(string="Noleggio Auto", default=False)


    #region Telefonia 
    Con_GestoreAttuale = fields.Selection([('nuova','Nuova Attivazione'), ('vuoto1', 'vuoto'), ('vuoto2', 'vuoto2')])
    Con_Tel_MetodoPagamento = fields.Selection([('iban','Iban'), ('cc', 'CC')])
    Con_OffertaAttuale = fields.Char(string='Offerta Attuale:')
    Con_CodMigrazione = fields.Char(string='Codice Migrazione:')
    Con_Num_Migrare = fields.Char(string='Numero da Migrare:')
    Con_Num_Sim = fields.Char(string='Numero SIM:')
    #Con_LineeAttive = fields.Char(string='N. Linee Attive:')
    #endregion

    #region Energia    
    #Con_Pod_ProvMervato = fields.Boolean(string="Provenienza mercato libero", default=False)
    #Con_Pod_AttDis = fields.Selection([('pod_attivo','Attivo'), ('pod_disattivo', 'Disattivo')])
    #Con_Pod_Distributore = fields.Char(string='Distributore di zona:')
    Con_Pod = fields.Char(string='POD:')
    Con_Pod_MetodoPagamento = fields.Selection([('iban','Iban'), ('bollettino', 'Bollettino'), ('finanziamento', 'Finanziamento')])
    Con_Pod_AttSocVendita = fields.Char(string="Attuale societa' vendita:")
    Con_Pod_Potenzakvw = fields.Char(string='Potenza KW:')
    Con_Pod_ConsAnnuo= fields.Char(string='Consumo annuo:')
    #Con_Pod_DataAttivazione= fields.Date(string='Data attivazione:')


    Con_Pdr = fields.Char(string='PDR:')
    Con_Pdr_AttSocVendita = fields.Char(string="Attuale societa' vendita:")
    #Con_Pdr_Distributore = fields.Char(string='Distributore di zona:')
    Con_Pdr_ConsAnnuo= fields.Char(string='Consumo annuo:')
    Con_Pdr_DataAttivazione= fields.Date(string='Data attivazione:')
    #Con_Pdr_Riscaldamento = fields.Boolean(string="Riscaldamento", default=False)
    #Con_Pdr_CottAcqua = fields.Boolean(string="Cottura e/o acqua", default=False)
    #Con_Pdr_AttDis = fields.Selection([('pod_attivo','Attivo'), ('pod_disattivo', 'Disattivo')])
    #endregion


    #region Fotovoltaico
    Con_Fotov_MetodoPagamento = fields.Selection([('iban','Iban'), ('cc', 'CC'), ('unicaTranche', 'Bonifico unica tranche'), ('multiTranche', 'Bonifico multi tranche'), ('finanziamento','Finanziamento')])
    Con_Fotov_Wallbox = fields.Boolean(string="Wallbox", default=False)
    Con_Fotov_PotenzaImp = fields.Char(string='Potenza impianto:')
    Con_Fotov_Potenzabatt = fields.Char(string='Potenza batteria accumolo:')
    Con_Fotov_Pompa = fields.Char(string='Pompa di calore:')
    #enregion

    #region NoleggioAuto
    Con_Auto_AutoVenduta = fields.Char(string='Auto venduta:')
    Con_Fotov_DurataNoleggio = fields.Char(string='Durata noleggio:')
    #Con_Auto_from_date = fields.Date(string="Register date")
    #Con_Auto_final_date = fields.Date(string="Last date")
    #Con_Auto_total_days = fields.Integer(string="Durata noleggio in gioni:")

    #@api.onchange(' Con_Auto_from_date', ' Con_Auto_final_date',' Con_Auto_total_days')
    #def calculate_date(self):
    #    if self.from_date and self.final_date:
    #        d1=datetime.strptime(str(self.from_date),'%Y-%m-%d') 
    #        d2=datetime.strptime(str(self.final_date),'%Y-%m-%d')
    #        d3=d2-d1
    #        self. Con_Auto_total_days=str(d3.days)
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
    