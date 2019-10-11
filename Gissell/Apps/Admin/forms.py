from django import forms
from .models import Persona

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