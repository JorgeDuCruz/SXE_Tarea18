# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pacientes(models.Model):
     _name = 'hospital.pacientes'
     _description = 'hospital.pacientes'

     name = fields.Char(string="Nombre del Paciente", required=True)
     last_name = fields.Char(string="Apellidos del Paciente", required=True)
     sintomas = fields.Char(string="Síntomas del Paciente", required=True)
     medicos_ids = fields.Many2many(comodel_name="hospital.medicos",
                                    relation="Diagnosticos",
                                    column1="paciente_id",
                                    column2="medico_id",
                                    string="Médicos",
                                    through='hospital.diagnostico'
                                    )



