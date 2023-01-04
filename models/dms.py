# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, _


class Users(models.Model):
    _name = 'dms.file'
    _inherit = ['dms.file']


    def open_file_upload(self):
        return{
            'res_model': 'contratti.contratto',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': self.env.ref('view_dms_file_new_form').id
            }
            
