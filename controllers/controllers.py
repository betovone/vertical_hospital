# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class VerticalHospitalPaciente(http.Controller):

    @http.route('/pacientes/consulta/<secuencia>/', type='json', auth='public', methods=['GET'])
    def get_paciente_por_secuencia(self, **kw):
        paciente = request.env['vertical_hospital.paciente'].sudo().search([ ('name', '=', kw['secuencia']) ])
        datos = {}
        if paciente:
            datos = {
                'seq': paciente.name,
                'name': paciente.nombre_apellido,
                'dni': paciente.dni,
                'state': paciente.state
            }
        
        return datos


