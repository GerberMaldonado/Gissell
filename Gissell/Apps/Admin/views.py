from django.views.generic import TemplateView, ListView, CreateView
from .models import Persona

# Create your views here.
class IndexView(TemplateView):
	template_name='home.html'

# Vistas para el CRUD de Persona
class PersonaLista(ListView):
	template_name = 'persona_list.html'
	model = Persona

class PersonaCreate(ListView):
	template_name = 'persona_create.html'
	model = Persona