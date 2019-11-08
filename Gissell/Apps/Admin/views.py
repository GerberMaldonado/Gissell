from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, View
from .models import Persona, TipoPersona, TipoPersonaPersona, TipoTerapia, Terapia, Donacion, TipoDonacion, Curso, \
    AsignacionCurso, Unidad, Nota 
from .forms import PersonaForm, TipoPersonaForm, TipoPersonaPersonaForm, TerapiaForm, TipoTerapiaForm, DonacionForm, \
    TipoDonacionForm, CursoForm, AsignacionForm, NotaForm, UnidadForm
from django.urls import reverse_lazy
from django.shortcuts import redirect, render

# Create your views here.

class IndexView(TemplateView):
	template_name='admin/home.html'

# Vistas para el CRUD de Persona
class PersonaLista(ListView):
	template_name = 'persona/persona_list.html'
	model = Persona

class PersonaCreate(CreateView):
    template_name = 'persona/persona_create.html'
    form_class = PersonaForm
    def get_success_url(self):
        return reverse_lazy('Admin:tipo_persona_persona_create') + '?register'

class PersonaActualizar(UpdateView):
    template_name = 'persona/persona_update.html'
    model = Persona
    form_class = PersonaForm
    def get_success_url(self):
        return reverse_lazy('Admin:persona_list') + '?rega'        

class PersonaEliminar(DeleteView):
    template_name='persona/persona_delete.html'	
    model = Persona
    form_class = PersonaForm 
    def get_success_url(self):
        return reverse_lazy('Admin:persona_list') + '?regd'           

# Vistas para el CRUD de Tipo Persona
class TipoPersonaLista(ListView):
	template_name = 'persona/tipo_persona_list.html'
	model = TipoPersona

class TipoPersonaCreate(CreateView):
    template_name = 'persona/tipo_persona_create.html'
    form_class = TipoPersonaForm	
    def get_success_url(self):
        return reverse_lazy('Admin:persona_create') + '?regtp' 

class TipoPersonaActualizar(UpdateView):
    template_name = 'persona/tipo_persona_update.html'
    model = TipoPersona
    form_class = TipoPersonaForm
    def get_success_url(self):
        return reverse_lazy('Admin:tipo_persona_list') + '?rega'          

class TipoPersonaEliminar(DeleteView):
    template_name='persona/tipo_persona_delete.html'	
    model = TipoPersona
    form_class = TipoPersonaForm    
    def get_success_url(self):
        return reverse_lazy('Admin:tipo_persona_list') + '?regd'   

# Vistas para el CRUD de Tipo Persona Persona
class TipoPersonaPersonaLista(ListView):
	template_name = 'persona/tipo_persona_persona_list.html'
	model = TipoPersonaPersona

class TipoPersonaPersonaCreate(CreateView):
    template_name = 'persona/tipo_persona_persona_create.html'
    form_class = TipoPersonaPersonaForm
    def get_success_url(self):
        return reverse_lazy('Admin:persona_list') + '?regtpp'

class TipoPersonaPersonaActualizar(UpdateView):
    template_name = 'persona/tipo_persona_persona_update.html'
    model = TipoPersonaPersona
    form_class = TipoPersonaPersonaForm
    def get_success_url(self):
        return reverse_lazy('Admin:tipo_persona_persona_list') + '?rega'        

class TipoPersonaPersonaEliminar(DeleteView):
    template_name='persona/tipo_persona_persona_delete.html'	
    model = TipoPersonaPersona
    form_class = TipoPersonaPersonaForm    
    def get_success_url(self):
        return reverse_lazy('Admin:tipo_persona_persona_list') + '?regd'   

# Vistas para el CRUD de Terapia
class TerapiaLista(ListView):
	template_name = 'terapia/terapia_list.html'
	model = TipoTerapia

class TerapiaCreate(CreateView):
    template_name = 'terapia/terapia_create.html'
    form_class = TipoTerapiaForm
    def get_success_url(self):
        return reverse_lazy('Admin:tipo_terapia_create') + '?register'

class TerapiaActualizar(UpdateView):
    template_name = 'terapia/terapia_update.html'
    model = TipoTerapia
    form_class = TipoTerapiaForm
    def get_success_url(self):
        return reverse_lazy('Admin:terapia_list') + '?rega'    

class TerapiaEliminar(DeleteView):
    template_name='terapia/terapia_delete.html'	
    model = TipoTerapia
    form_class = TipoTerapiaForm    
    def get_success_url(self):
        return reverse_lazy('Admin:terapia_list') + '?regd'    

# Vistas para el CRUD de Tipo Terapia
class TipoTerapiaLista(ListView):
	template_name = 'terapia/tipo_terapia_list.html'
	model = Terapia

class TipoTerapiaCreate(CreateView):
    template_name = 'terapia/tipo_terapia_create.html'
    form_class = TerapiaForm
    def get_success_url(self):
        return reverse_lazy('Admin:terapia_list') + '?register'

class TipoTerapiaActualizar(UpdateView):
    template_name = 'terapia/tipo_terapia_update.html'
    model = Terapia
    form_class = TerapiaForm    
    def get_success_url(self):
        return reverse_lazy('Admin:tipo_terapia_list') + '?rega'     

class TipoTerapiaEliminar(DeleteView):
    template_name='terapia/tipo_terapia_delete.html'	
    model = Terapia
    form_class = TerapiaForm    
    def get_success_url(self):
        return reverse_lazy('Admin:tipo_terapia_list') + '?regd' 

# Vistas para el CRUD de Donacion
class DonacionLista(ListView):
	template_name = 'donacion/donacion_list.html'
	model = Donacion

class DonacionCreate(CreateView):
    template_name = 'donacion/donacion_create.html'
    form_class = DonacionForm
    def get_success_url(self):
        return reverse_lazy('Admin:donacion_list') + '?register'

class DonacionActualizar(UpdateView):
    template_name = 'donacion/donacion_update.html'
    model = Donacion
    form_class = DonacionForm
    def get_success_url(self):
        return reverse_lazy('Admin:donacion_list') + '?rega'

class DonacionEliminar(DeleteView):
    template_name='donacion/donacion_delete.html'	
    model = Donacion
    form_class = DonacionForm    
    def get_success_url(self):
        return reverse_lazy('Admin:donacion_list') + '?regd'

# Vistas para el CRUD de Tipo Donacion
class TipoDonacionLista(ListView):
	template_name = 'donacion/tipo_donacion_list.html'
	model = TipoDonacion

class TipoDonacionCreate(CreateView):
    template_name = 'donacion/tipo_donacion_create.html'
    form_class = TipoDonacionForm
    def get_success_url(self):
        return reverse_lazy('Admin:donacion_create') + '?regt'

class TipoDonacionActualizar(UpdateView):
    template_name = 'donacion/tipo_donacion_update.html'
    model = TipoDonacion
    form_class = TipoDonacionForm
    def get_success_url(self):
        return reverse_lazy('Admin:tipo_donacion_list') + '?rega'

class TipoDonacionEliminar(DeleteView):
    template_name='donacion/tipo_donacion_delete.html'	
    model = TipoDonacion
    form_class = TipoDonacionForm    
    def get_success_url(self):
        return reverse_lazy('Admin:tipo_donacion_list') + '?regd'

# Vistas para el CRUD de Curso
class CursoLista(ListView):
	template_name = 'curso/curso_list.html'
	model = Curso

class CursoCreate(CreateView):
    template_name = 'curso/curso_create.html'
    form_class = CursoForm
    def get_success_url(self):
        return reverse_lazy('Admin:asignacion_create') + '?register'

class CursoActualizar(UpdateView):
    template_name = 'curso/curso_update.html'
    model = Curso
    form_class = CursoForm
    def get_success_url(self):
        return reverse_lazy('Admin:curso_list') + '?rega'

class CursoEliminar(DeleteView):
    template_name='curso/curso_delete.html'	
    model = Curso
    form_class = CursoForm    
    def get_success_url(self):
        return reverse_lazy('Admin:curso_list') + '?regd'

# Vistas para el CRUD de Curso
class AsignacionLista(ListView):
	template_name = 'curso/asi_curso_list.html'
	model = AsignacionCurso

class AsignacionCreate(CreateView):
    template_name = 'curso/asi_curso_create.html'
    form_class = AsignacionForm
    def get_success_url(self):
        return reverse_lazy('Admin:asignacion_list') + '?register'

class AsignacionActualizar(UpdateView):
    template_name = 'curso/asi_curso_update.html'
    model = AsignacionCurso
    form_class = AsignacionForm
    def get_success_url(self):
        return reverse_lazy('Admin:asignacion_list') + '?rega'

class AsignacionEliminar(DeleteView):
    template_name='curso/asi_curso_delete.html'	
    model = AsignacionCurso
    form_class = AsignacionForm    
    def get_success_url(self):
        return reverse_lazy('Admin:asignacion_list') + '?regd'             

# Vistas para el CRUD de Curso
class NotaLista(ListView):
	template_name = 'nota/nota_list.html'
	model = Nota

class NotaCreate(CreateView):
    template_name = 'nota/nota_create.html'
    form_class = NotaForm
    def get_success_url(self):
        return reverse_lazy('Admin:nota_list') + '?register'

class NotaActualizar(UpdateView):
    template_name = 'nota/nota_update.html'
    model = Nota
    form_class = NotaForm
    def get_success_url(self):
        return reverse_lazy('Admin:nota_list') + '?rega'

class NotaEliminar(DeleteView):
    template_name='nota/nota_delete.html'	
    model = Nota
    form_class = NotaForm    
    def get_success_url(self):
        return reverse_lazy('Admin:nota_list') + '?regd'

# Vistas para el CRUD de Unidad
class UnidadLista(ListView):
	template_name = 'nota/unidad_list.html'
	model = Unidad

class UnidadCreate(CreateView):
    template_name = 'nota/unidad_create.html'
    form_class = UnidadForm
    def get_success_url(self):
        return reverse_lazy('Admin:nota_create') + '?register'

class UnidadActualizar(UpdateView):
    template_name = 'nota/unidad_update.html'
    model = Unidad
    form_class = UnidadForm
    def get_success_url(self):
        return reverse_lazy('Admin:unidad_list') + '?rega'

class UnidadEliminar(DeleteView):
    template_name='nota/unidad_delete.html'	
    model = Unidad
    form_class = UnidadForm    
    def get_success_url(self):
        return reverse_lazy('Admin:unidad_list') + '?regd'

class report(View):
    pdf = canvas.Canvas("Hola")
    pdf.save()