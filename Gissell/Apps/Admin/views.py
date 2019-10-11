from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Persona
from .forms import PersonaForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
# Create your views here.

# Redireccionamiento si no esta autenticado
class StaffRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

class IndexView(StaffRequiredMixin, TemplateView):
	template_name='admin/home.html'

# Vistas para el CRUD de Persona
class PersonaLista(StaffRequiredMixin, ListView):
	template_name = 'persona/persona_list.html'
	model = Persona

class PersonaCreate(StaffRequiredMixin, CreateView):
	template_name = 'persona/persona_create.html'
	form_class = PersonaForm
	success_url = reverse_lazy('Admin:persona_list')

class PersonaActualizar(StaffRequiredMixin, UpdateView):
    template_name = 'persona/persona_update.html'
    model = Persona
    form_class = PersonaForm
    success_url = reverse_lazy('Admin:persona_list')

class PersonaEliminar(StaffRequiredMixin, DeleteView):
    template_name='persona/persona_delete.html'	
    model = Persona
    form_class = PersonaForm    
    success_url = reverse_lazy('Admin:persona_list')