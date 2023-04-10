from odoo import _, models, fields, api, exceptions
from dateutil.relativedelta import relativedelta
from odoo.tools import float_compare

class VHPaciente(models.Model):
	_name = "vertical_hospital.paciente"
	_description = "Paciente del hospital Vertical"
	_inherit = ['mail.thread', 'mail.activity.mixin']
	#_inherit = 'mail.thread'
	_order = "name desc"
	name = fields.Char(size=10, string='Secuencia', readonly=True, index=True)
	nombre_apellido = fields.Char(size=100, string='Nombre y Apellido', required=True)
	dni = fields.Char(size=10, string="DNI", required=True)
	tratamientos_realizados = fields.Many2many("vertical_hospital.tratamiento", 
					    						string="Tratamientos",
												ondelete='restrict' )
	state = fields.Selection(selection=[ 
		                            ('borrador', 'Borrador'), 
				                    ('alta', 'Alta'), 
				                    ('baja' , 'Baja')
				                ], 
				                string="Estado", required=True, 
				                default='borrador')


	@api.constrains('dni')
	def _check_dni(self):
		print(f"DNI= {self.dni}")
		if not self.dni.isdigit():
			raise exceptions.ValidationError("Ingrese sólo números en el DNI")


	@api.model
	def create(self, vals):
		vals['name'] = self.env['ir.sequence'].next_by_code('vertical_hospital.paciente')
		return super(VHPaciente, self).create(vals)

	
	def write(self, vals):
		res = super().write(vals)
		body = ''
		obj = self.search([ ('id', '=', self.id) ])
		if 'dni' in vals:
			body="El DNI ha cambiado a %s <br>" % vals['dni']
		
		if 'state' in vals:
			body += "El ESTADO ha cambiado a %s" % vals['state']

		self.message_post(body=body)
		return res




class VHTratamiento(models.Model):
	_name = "vertical_hospital.tratamiento"
	_description = "Tratamiento del paciente del hospital Vertical"
	_order = "name desc"

	name = fields.Char(size=256, string="Código", required=True)
	nombre = fields.Char(size=256, string="Nombre", required=True)
	medico_tratante = fields.Char(size=256, string="Médico tratante", required=True)

	_sql_constraints = [
        ('check_name', 'unique(name)', 'El código ya existe.'), 
    ]
	@api.constrains('name')
	def _check_name(self):
		for record in self:
			if '026' in record.name:
				raise exceptions.ValidationError("El Código no puede contener la secuencia '026' ")


	def name_get(self):
		result = []
		for t in self:
			name = f'{t.name} {t.nombre}'
			result.append((t.id, name))
		return result


