from django import forms
from .models import Persona, TipoPersona, TipoPersonaPersona, TipoTerapia, Terapia, Donacion, TipoDonacion, Curso, \
	AsignacionCurso, Nota, Unidad

class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = '__all__'
		widgets = {
		'nombre': forms.TextInput(attrs={'class': 'form-control mb3', 'type': 'text'}),
		'apellido': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
		'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'min': '1900-01-01', 'max': '2019-11-08'}),
		'telefono': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'required': '', 'min': '11111111', 'max': '99999999'}),
		'direccion': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),		
		}
				
class TipoPersonaForm(forms.ModelForm):
	class Meta:
		model = TipoPersona
		fields = '__all__'
		widgets = {
		'tipo_persona': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),		
		}

class TipoPersonaPersonaForm(forms.ModelForm):
	class Meta:
		model = TipoPersonaPersona
		fields = '__all__'
		widgets = {
		'persona_id': forms.Select(attrs={'class': 'form-control'}),		
		'tipo_persona_id': forms.Select(attrs={'class': 'form-control'}),
		}

class TipoTerapiaForm(forms.ModelForm):
	class Meta:
		model = TipoTerapia
		fields = '__all__'
		widgets = {
		'tipo_terapia': forms.TextInput(attrs={'class': 'form-control mb3', 'type': 'text'}),				
		'sesiones': forms.TextInput(attrs={'class': 'form-control', 'type': 'datetime'}),		
		'avances': forms.TextInput(attrs={'class': 'form-control', 'type':'text'}),
		'descripcion': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
		}

class TerapiaForm(forms.ModelForm):
	class Meta:
		model = Terapia
		fields = '__all__'
		widgets = {
		'tipo_terapia_id': forms.Select(attrs={'class': 'form-control'}),		
		'tipo_persona_persona_id': forms.Select(attrs={'class': 'form-control'}),
		}

class DonacionForm(forms.ModelForm):
	class Meta:
		model = Donacion
		fields = '__all__'
		widgets = {
		'monto': forms.TextInput(attrs={'class': 'form-control mb3', 'type': 'number', 'required':'', 'min': '1'}),
		'tipo_donacion_id': forms.Select(attrs={'class': 'form-control'}),		
		'tipo_persona_persona_id': forms.Select(attrs={'class': 'form-control'}),
		}

class TipoDonacionForm(forms.ModelForm):
	class Meta:
		model = TipoDonacion
		fields = '__all__'
		widgets = {
		'tipo_donacion': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
		}
class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso
		fields = '__all__'
		widgets = {
		'curso': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
		}

class AsignacionForm(forms.ModelForm):
	class Meta:
		model = AsignacionCurso
		fields = '__all__'
		widgets = {		
		'curso_id': forms.Select(attrs={'class': 'form-control'}),		
		'tipo_persona_persona_id': forms.Select(attrs={'class': 'form-control'}),
		}

class NotaForm(forms.ModelForm):
	class Meta:
		model = Nota
		fields = '__all__'
		widgets = {		
		'nota': forms.TextInput(attrs={'class': 'form-control mb3', 'type': 'number', 'min': '1', 'max': '100'}),
		'unidad_id': forms.Select(attrs={'class': 'form-control'}),		
		'tipo_persona_persona_id': forms.Select(attrs={'class': 'form-control'}),
		}

class UnidadForm(forms.ModelForm):
	class Meta:
		model = Unidad
		fields = '__all__'
		widgets = {		
		'unidad': forms.TextInput(attrs={'class': 'form-control mb3', 'type': 'text'}),		
		}														