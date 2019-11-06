from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Persona, TipoPersona, TipoPersonaPersona
from .forms import PersonaForm, TipoPersonaForm, TipoPersonaPersonaForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
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
    modelo = TipoPersonaPersona
    template_name = 'persona/persona_create.html'
    form_class = TipoPersonaPersonaForm
    second_form_class = PersonaForm    
    def get_success_url(self):
        return reverse_lazy('Admin:persona_list') + '?register'

    def get_context_data(self, **Kwargs):
        context = super(PersonaCreate, self).get_context_data(**Kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **Kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else: 
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


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

# Vistas para el CRUD de Tipo Persona
class TipoPersonaLista(StaffRequiredMixin, ListView):
	template_name = 'persona/tipo_persona_list.html'
	model = TipoPersona

class TipoPersonaCreate(StaffRequiredMixin, CreateView):
	template_name = 'persona/tipo_persona_create.html'
	form_class = TipoPersonaForm
	success_url = reverse_lazy('Admin:tipo_persona_list')

class TipoPersonaActualizar(StaffRequiredMixin, UpdateView):
    template_name = 'persona/tipo_persona_update.html'
    model = TipoPersona
    form_class = TipoPersonaForm
    success_url = reverse_lazy('Admin:tipo_persona_list')

class TipoPersonaEliminar(StaffRequiredMixin, DeleteView):
    template_name='persona/tipo_persona_delete.html'	
    model = TipoPersona
    form_class = TipoPersonaForm    
    success_url = reverse_lazy('Admin:tipo_persona_list')

# Vistas para el CRUD de Tipo Persona Persona
class TipoPersonaPersonaLista(StaffRequiredMixin, ListView):
	template_name = 'persona/tipo_persona_persona_list.html'
	model = TipoPersonaPersona

class TipoPersonaPersonaCreate(StaffRequiredMixin, CreateView):
	template_name = 'persona/tipo_persona_persona_create.html'
	form_class = TipoPersonaPersonaForm
	success_url = reverse_lazy('Admin:tipo_persona_persona_list')

class TipoPersonaPersonaActualizar(StaffRequiredMixin, UpdateView):
    template_name = 'persona/tipo_persona_persona_update.html'
    model = TipoPersonaPersona
    form_class = TipoPersonaPersonaForm
    success_url = reverse_lazy('Admin:tipo_persona_persona_list')

class TipoPersonaPersonaEliminar(StaffRequiredMixin, DeleteView):
    template_name='persona/tipo_persona_persona_delete.html'	
    model = TipoPersonaPersona
    form_class = TipoPersonaPersonaForm    
    success_url = reverse_lazy('Admin:tipo_persona_persona_list')

# Vistas para el CRUD de Persona
class PersonaListarEnPersona(StaffRequiredMixin, ListView):
	template_name = 'persona/persona_list.html'
	model = Persona    