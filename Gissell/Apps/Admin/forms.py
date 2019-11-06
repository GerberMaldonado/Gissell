from django import forms
from .models import Persona, TipoPersona, TipoPersonaPersona

class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = '__all__'
		widgets = {
		'nombre': forms.TextInput(attrs={'class': 'form-control mb3', 'type': 'text'}),
		'apellido': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
		'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
		'telefono': forms.TextInput(attrs={'class': 'form-control', 'type': 'phone'}),
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