# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Medicos(models.Model):
     _name = 'hospital.medicos'
     _description = 'hospital.medicos'

     name = fields.Char(string="Nombre del Médico", required=True)
     last_name = fields.Char(string="Apellidos del Médico", required=True)
     num_cole = fields.Integer(string="Número del colegiado",required=True)
     pacientes_ids = fields.Many2many(comodel_name="hospital.pacientes",
                                    relation="Diagnosticos",
                                    column1="medico_id",
                                    column2="paciente_id",
                                    string="Pacientes",
                                    through='hospital.diagnostico'
                                    )