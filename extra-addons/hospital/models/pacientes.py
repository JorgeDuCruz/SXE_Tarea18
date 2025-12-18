# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pacientes(models.Model):
     _name = 'hospital.pacientes'
     _description = 'hospital.pacientes'

     name = fields.Char(string="Nombre del Paciente", required=True)
     last_name = fields.Char(string="Apellidos del Paciente", required=True)
     sintomas = fields.Char(string="Síntomas del Paciente", required=True)




