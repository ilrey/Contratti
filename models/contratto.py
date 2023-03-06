from dataclasses import field
from email.policy import default
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ContrattiContratto(models.Model):
    _name = "contratti.contratto"
    _description = "Contratto"

    # region Default
    Con_CognomeClienteContratto = fields.Char(string="Cognome")
    Con_NomeCliente = fields.Char(string="Nome")
    Con_CodFiscaleCliente = fields.Char(string="Codice Fiscale")
    Con_TipoDocumento = fields.Selection(
        [
            ("CARTA_IDENTITA", "CARTA IDENTITA"),
            ("PATENTE", "PATENTE"),
            ("PASSAPORTO", "PASSAPORTO"),
        ]
    )
    Con_Numero = fields.Char(string="Numero")
    Con_RilasciatoDa = fields.Selection(
        [
            ("COMUNE", "COMUNE"),
            ("MCTC", "MCTC"),
            ("UCO", "UCO"),
            ("QUESTURA", "QUESTURA"),
        ]
    )
    Con_DataRilascio = fields.Date(string="Data rilascio")
    Con_Telefono = fields.Char(string="Telefono")
    Con_Cellulare = fields.Char(string="Cellulare")
    Con_Email = fields.Char(string="Email")
    Con_Pec = fields.Char(string="PEC")
    Con_Indirizzo = fields.Char(string="Indirizzo")
    Con_Civico = fields.Char(string="N.Civico")
    Con_Scala = fields.Char(string="Scala")
    Con_Interno = fields.Char(string="Interno")
    Con_Citta = fields.Char(string="Citta'")
    Con_Note = fields.Html("Note")
    Con_Documento = fields.Binary(string="Documento cliente")
    # endregion

    Con_Telefonia = fields.Boolean(string="Telefonia", default=False)
    Con_Pod_bool = fields.Boolean(string="Luce", default=False)
    Con_Pdr_bool = fields.Boolean(string="Gas", default=False)
    Con_Fotov_bool = fields.Boolean(string="Fotovoltaico", default=False)
    Con_Auto_bool = fields.Boolean(string="Noleggio Auto", default=False)

    # region Telefonia
    Con_GestoreAttuale = fields.Selection(
        [
            ("NUOVA", "NUOVA ATTIVAZIONE"),
            ("TIM", "TIM"),
            ("VODAFONE", "VODAFONE"),
            ("WINDTRE", "WIND TRE"),
            ("ILIAD_ITALIA", "ILIAD ITALIA"),
            ("FASTWEB", "FASTWEB"),
            ("COOPVOCE", "COOPVOCE"),
            ("HO", "HO."),
            ("KENA", "KENA MOBILE"),
            ("LYCAMOBILE", "LYCAMOBILE"),
            ("POSTEMOBILE", "POSTEMOBILE"),
            ("RABONAMOBILE", "RABONA MOBILE"),
            ("TISCALI", "TISCALI"),
            ("ILLIAD", "ILLIAD"),
        ]
    )
    Con_Tel_MetodoPagamento = fields.Selection([("IBAN", "IBAN"), ("CC", "CC")])
    Con_OffertaAttuale = fields.Char(string="Offerta Attuale:")
    Con_CodMigrazione = fields.Char(string="Codice Migrazione:")
    Con_Num_Migrare = fields.Char(string="Numero da Migrare:")
    Con_Num_Sim = fields.Char(string="Numero SIM:")
    Con_Tel_Documento = fields.Binary(string="Documento telefonia")
    # endregion

    # region Energia
    Con_Pod = fields.Char(string="POD:")
    Con_Pod_MetodoPagamento = fields.Selection(
        [
            ("IBAN", "IBAN"),
            ("BOLLETTINO", "BOLLETTINO"),
            ("FINANZIAMENTO", "FINANZIAMENTO"),
        ]
    )
    Con_Pod_AttSocVendita = fields.Char(string="Attuale societa' vendita:")
    Con_Pod_Potenzakvw = fields.Char(string="Potenza KW:")
    Con_Pod_ConsAnnuo = fields.Char(string="Consumo annuo:")
    Con_Pod_Documento = fields.Binary(string="Documento Energia")
    # Con_Pod_DataAttivazione= fields.Date(string='Data attivazione:')

    Con_Pdr = fields.Char(string="PDR:")
    Con_Pdr_AttSocVendita = fields.Char(string="Attuale societa' vendita:")
    Con_Pdr_ConsAnnuo = fields.Char(string="Consumo annuo:")
    Con_Pdr_PotenzaSMC = fields.Char(string="Potenza Standard Metro Cubo:")
    Con_Pdr_Documento = fields.Binary(string="Documento Gas")
    # endregion

    # region Fotovoltaico
    Con_Fotov_MetodoPagamento = fields.Selection(
        [
            ("UNICATRANCHE", "BONIFICO UNICA TRANCHE"),
            ("MULTITRANCHE", "BONIFICO MULTI TRANCHE"),
            ("FINANZIAMENTO", "FINANZIAMENTO"),
        ]
    )
    Con_Fotov_Wallbox = fields.Boolean(string="Wallbox", default=False)
    Con_Fotov_PotenzaImp = fields.Char(string="Potenza impianto:")
    Con_Fotov_Potenzabatt = fields.Char(string="Potenza batteria accumolo:")
    Con_Fotov_Pompa = fields.Char(string="Pompa di calore:")
    Con_Fotov_Documento = fields.Binary(string="Documento Fotovoltaico")
    # enregion

    # region NoleggioAuto
    Con_Auto_AutoVenduta = fields.Char(string="Auto venduta:")
    Con_Auto_Documento = fields.Binary(string="Documento Auto")
    Con_Auto_DurataNoleggio = fields.Char(string="Durata noleggio:")
    # enregion

    active = fields.Boolean(string="Active", default=True)
    user_id = fields.Many2one(
        "res.users", tracking=True, default=lambda self: self.env.user
    )
    partner_ids = fields.Many2many(
        "res.partner", tracking=True
    )
    # user_id2 = fields.Char("Current User", default=lambda self: self.env.uid)

    def open_file_upload(self):
        return {
            "res_model": "dms.file",
            #'res_id': 12,
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "view_id": self.env.ref("dms.view_dms_file_form").id,
        }

    @api.model
    def create(self, vals):
        for i in list(vals):
            if type(vals[i]) != bool and type(vals[i]) != int:
                if type(vals[i]) != list:
                    vals[i] = vals[i].upper()
        return super(ContrattiContratto, self).create(vals)

    @api.model
    def write(self, vals):
        for i in list(vals):
            if type(vals[i]) != bool and type(vals[i]) != int:
                if type(vals[i]) != list:
                    vals[i] = vals[i].upper()
        return super(ContrattiContratto, self).write(vals)

    # def buttone_prova(self):
    #    delta = self.env['dms.file'].write({'name' : 'provafie'})
    #    return delta

    # calendar_module
    # def map_url(self):
    #    url_string = ("https://www.google.com/maps/dir//+{},+{},+{}".format(self.x_indirizzo, self.x_civico, self.x_citta))
    #    if False in (self.x_indirizzo, self.x_civico, self.x_citta):
    #        raise ValidationError(_("Indirizzo non completo"))
    #    else:
    #        return{
    #            'type': 'ir.actions.act_url',
    #            'url': url_string
    #            }
#    <?xml version="1.0"?>
#<form string="Meetings">
#	<div attrs="{'invisible': [('recurrence_id','=',False)]}" class="alert alert-info oe_edit_only" role="status">
#		<p>Edit recurring event</p>
#		<field name="recurrence_update" widget="radio"/>
#	</div>
#	<sheet>
#		<div class="oe_button_box" name="button_box">
#			<button string="Document" icon="fa-bars" type="object" name="action_open_calendar_event" attrs="{'invisible': ['|', ('res_model', '=', False), ('res_id', '=', False)]}"/>
#		</div>
#		<widget name="web_ribbon" title="Archived" bg_color="bg-danger" attrs="{'invisible': [('active', '=', True)]}"/>
#		<field name="res_model" invisible="1"/>
#		<field name="res_id" invisible="1"/>
#		<field name="attendee_status" invisible="1"/>
#		<field name="active" invisible="1"/>
#		<div class="oe_title mb-3">
#			<div>
#				<label for="name"/>
#			</div>
#			<h1>
#				<field name="name" placeholder="e.g. Business Lunch"/>
#			</h1>
#		</div>
#		<div class="d-flex align-items-baseline">
#		  <field name="utente_loggato" invisible="1"/>
#			<field name="partner_ids" widget="many2manyattendee" placeholder="Select attendees..." context="{'force_email':True}" attrs="{'readonly': [('utente_loggato','not in', ['2', '18'])]}" domain="[('type','!=','private')]" class="oe_inline o_calendar_attendees"/>
#			<div name="send_buttons" class="sm-2">
#				<button name="action_open_composer" help="Send Email to attendees" type="object" string=" EMAIL" icon="fa-envelope"/>
#			</div>
#		</div>
#		<notebook>
#			<page name="page_details" string="Meeting Details">
#				<group>
#					<group>

#						<field name="start_date" string="Starting at" attrs="{'required': [('allday','=',True)], 'invisible': [('allday','=',False)]}" force_save="1"/>
#						<field name="stop_date" string="Ending at" attrs="{'required': [('allday','=',True)],'invisible': [('allday','=',False)]}" force_save="1"/>
#						<field name="start" string="Starting at" attrs="{'required': [('allday','=',False)], 'invisible': [('allday','=',True)]}"/>
#						<field name="stop" string="Ending At" attrs="{'invisible': [('allday','=',True)]}"/>
#						<label for="duration" attrs="{'invisible': [('allday','=',True)]}"/>
#						<div attrs="{'invisible': [('allday','=',True)]}">
#							<field name="duration" widget="float_time" string="Duration" class="oe_inline"/>
#							<span> hours</span>
#						</div>
#						<field name="allday" force_save="1"/>
#						<field name="event_tz" attrs="{'invisible': [('recurrency', '=', False)]}"/>
#					</group>
#					<group>
#						<field name="alarm_ids" widget="many2many_tags" options="{'no_quick_create': True}"/>
#						<!-- <field name="location"/> -->
#						<field name="videocall_location"/>
#						<field name="user_id" widget="many2one_avatar_user"/>
#						<!-- <field name="categ_ids" widget="many2many_tags" options="{'color_field': 'color', 'no_create_edit': True}"/> -->
#					</group>
#				</group>
#				<group>
#					<field name="description"/>
#				</group>
#			</page>
#			<page name="page_options" string="Options" invisible="1">
#				<group>
#					<div>
#						<group>
#							<field name="recurrency"/>
#						</group>
#						<div attrs="{'invisible': [('recurrency', '=', False)]}">
#							<group>
#								<label for="interval"/>
#								<div class="o_col">
#									<div class="o_row">
#										<field name="interval" attrs="{'required': [('recurrency', '=', True)]}"/>
#										<field name="rrule_type" attrs="{'required': [('recurrency', '=', True)]}"/>
#									</div>
#									<widget name="week_days" attrs="{'invisible': [('rrule_type', '!=', 'weekly')]}"/>
#								</div>
#								<label string="Until" for="end_type"/>
#								<div class="o_row">
#									<field name="end_type" attrs="{'required': [('recurrency', '=', True)]}"/>
#									<field name="count" attrs="{'invisible': [('end_type', '!=', 'count')], 'required': [('recurrency', '=', True)]}"/>
#									<field name="until" attrs="{'invisible': [('end_type', '!=', 'end_date')], 'required': [('end_type', '=', 'end_date'), ('recurrency', '=', True)]}"/>
#								</div>
#							</group>
#							<group attrs="{'invisible': [('rrule_type', '!=', 'monthly')]}">
#								<label string="Day of Month" for="month_by"/>
#								<div class="o_row">
#									<field name="month_by"/>
#									<field name="day" attrs="{'required': [('month_by', '=', 'date'), ('rrule_type', '=', 'monthly')],                                                             'invisible': [('month_by', '!=', 'date')]}"/>
#									<field name="byday" string="The" attrs="{'required': [('recurrency', '=', True), ('month_by', '=', 'day'), ('rrule_type', '=', 'monthly')],                                                             'invisible': [('month_by', '!=', 'day')]}"/>
#									<field name="weekday" nolabel="1" attrs="{'required': [('recurrency', '=', True), ('month_by', '=', 'day'), ('rrule_type', '=', 'monthly')],                                                             'invisible': [('month_by', '!=', 'day')]}"/>
#								</div>
#							</group>
#						</div>
#					</div>
#					<group>
#						<field name="privacy"/>
#						<field name="show_as"/>
#						<field name="recurrence_id" invisible="1"/>
#					</group>
#				</group>
#			</page>

#			<page name="page_invitations" string="Invitations" groups="base.group_no_one" invisible="1">
#				<button name="action_sendmail" type="object" string="Send Invitations" icon="fa-envelope" class="oe_link"/>
#				<field name="attendee_ids" widget="one2many" mode="tree,kanban" readonly="1">
#					<tree string="Invitation details" editable="top" create="false" delete="false">
#						<field name="partner_id"/>
#						<field name="email" widget="email"/>
#						<field name="phone" widget="phone"/>
#						<field name="state"/>

#						<button name="do_tentative" states="needsAction,declined,accepted" string="Uncertain" type="object" icon="fa-asterisk"/>
#						<button name="do_accept" string="Accept" states="needsAction,tentative,declined" type="object" icon="fa-check text-success"/>
#						<button name="do_decline" string="Decline" states="needsAction,tentative,accepted" type="object" icon="fa-times-circle text-danger"/>
#					</tree>
#					<kanban class="o_kanban_mobile" create="false" delete="false">
#						<field name="partner_id"/>
#						<field name="state"/>
#						<field name="email" widget="email"/>

#						<templates>
#							<t t-name="kanban-box">
#								<div class="d-flex flex-column justify-content-between">
#									<field name="partner_id"/>
#									<field name="email" widget="email"/>
#									<span>
#										Status: <field name="state"/>
#									</span>

#									<div class="text-right">
#										<button name="do_tentative" states="needsAction,declined,accepted" string="Uncertain" type="object" class="btn fa fa-asterisk"/>
#										<button name="do_accept" states="needsAction,tentative,declined" string="Accept" type="object" class="btn fa fa-check text-success"/>
#										<button name="do_decline" states="needsAction,tentative,accepted" string="Decline" type="object" class="btn fa fa-times-circle text-danger"/>
#									</div>
#								</div>
#							</t>
#						</templates>
#					</kanban>
#				</field>
#			</page>
#			<page name="dettagli_cliente" string="Dettagli Cliente">
#				<group>
#					<group>
#						<field name="x_nome_cliente" string="Nome Cliente"/>
#						<field name="x_cognome_cliente" string="Cognome Cliente"/>
#						<field name="x_numero_cliente" string="Numero Cliente"/>
#						<field name="x_esito_appuntamento" string="Esito"/>
#					</group>
#					<group>
#						<field name="x_indirizzo"/>
#						<field name="x_civico"/>
#						<field name="x_scala"/>
#						<field name="x_interno"/>
#						<label for="x_citta"/>
#						<div class="o_row">
#							<field name="x_citta"/>
#							<button name="map_url" type="object" icon="fa-map-marker"></button>
#						</div>
#						<field name="x_carica_pdf" string="" attrs="{'invisible': [('x_esito_appuntamento', '!=', 'nd')]}"/>
#						<button name="carica_contratto" type="object" context="{'default_Con_CognomeClienteContratto': x_cognome_cliente,
#                                  'default_Con_NomeCliente': x_nome_cliente, 
#                                  'default_Con_Cellulare': x_numero_cliente,
#                                  'default_Con_Indirizzo': x_indirizzo,
#                                  'default_Con_Civico': x_civico,
#                                  'default_Con_Scala': x_scala,
#                                  'default_Con_Interno': x_interno,
#                                  'default_Con_Citta': x_citta}" string="Carica/Visualizza Contratto" attrs="{'invisible': [('x_esito_appuntamento', '!=', 'POSITIVO')]}"></button>
#					</group>
#				</group>
#				<group>
#					<field name="description" string="Note Dettagliate Esito"/>
#				</group>
#			</page>
#		</notebook>
#	</sheet>
#	<!-- <div class="oe_chatter">
#                    <field name="message_follower_ids"/>
#                    <field name="message_ids"/>
#                </div> -->
#</form>


