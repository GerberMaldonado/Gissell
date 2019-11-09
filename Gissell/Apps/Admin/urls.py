"""Gissell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import include, path
from .views import IndexView, PersonaLista, PersonaCreate, PersonaActualizar, PersonaEliminar, \
    TipoPersonaLista, TipoPersonaCreate, TipoPersonaActualizar, TipoPersonaEliminar, \
    TipoPersonaPersonaLista, TipoPersonaPersonaCreate, TipoPersonaPersonaActualizar, TipoPersonaPersonaEliminar, \
    TerapiaLista, TerapiaCreate, TerapiaActualizar, TerapiaEliminar, TipoTerapiaLista, TipoTerapiaCreate, \
    TipoTerapiaActualizar, TipoTerapiaEliminar, DonacionLista, DonacionCreate, DonacionActualizar, DonacionEliminar, \
    TipoDonacionCreate, TipoDonacionLista, TipoDonacionActualizar, TipoDonacionEliminar, CursoLista, CursoCreate, \
    CursoActualizar, CursoEliminar, AsignacionLista, AsignacionCreate, AsignacionActualizar, AsignacionEliminar, \
    NotaLista, NotaCreate, NotaActualizar, NotaEliminar, UnidadLista, UnidadCreate, UnidadActualizar, UnidadEliminar, \
    generar_pdf_personas, generar_pdf_notas

app_name = 'Admin'

urlpatterns = [
    path('', login_required(IndexView.as_view()), name='Home'),
    # Persona
    path('lista-persona', login_required(PersonaLista.as_view()), name='persona_list'),
    path('crear-persona', login_required(PersonaCreate.as_view()), name='persona_create'),
    path('actualizar-persona/<int:pk>/', login_required(PersonaActualizar.as_view()), name='persona_update'),
    path('eliminar-persona/<int:pk>/', login_required(PersonaEliminar.as_view()), name='persona_delete'),
    # Tipo Persona
    path('lista-tipo-persona', login_required(TipoPersonaLista.as_view()), name='tipo_persona_list'),
    path('crear-tipo-persona', login_required(TipoPersonaCreate.as_view()), name='tipo_persona_create'),
    path('actualizar-tipo-persona/<int:pk>/', login_required(TipoPersonaActualizar.as_view()), name='tipo_persona_update'),
    path('eliminar-tipo-persona/<int:pk>/', login_required(TipoPersonaEliminar.as_view()), name='tipo_persona_delete'),
    # Tipo Persona Persona
    path('lista-tipo-persona-persona', login_required(TipoPersonaPersonaLista.as_view()), name='tipo_persona_persona_list'),
    path('crear-tipo-persona-persona', login_required(TipoPersonaPersonaCreate.as_view()), name='tipo_persona_persona_create'),
    path('actualizar-tipo-persona/persona/<int:pk>/', login_required(TipoPersonaPersonaActualizar.as_view()), name='tipo_persona_persona_update'),
    path('eliminar-tipo-persona/persona/<int:pk>/', login_required(TipoPersonaPersonaEliminar.as_view()), name='tipo_persona_persona_delete'),
    # Terapia
    path('lista-terapia', login_required(TerapiaLista.as_view()), name='terapia_list'),
    path('crear-terapia', login_required(TerapiaCreate.as_view()), name='terapia_create'),
    path('actualizar-terapia/<int:pk>/', login_required(TerapiaActualizar.as_view()), name='terapia_update'),
    path('eliminar-terapia/<int:pk>/', login_required(TerapiaEliminar.as_view()), name='terapia_delete'),
    # Tipo Terapia
    path('lista-tipo-terapia', login_required(TipoTerapiaLista.as_view()), name='tipo_terapia_list'),
    path('crear-tipo-terapia', login_required(TipoTerapiaCreate.as_view()), name='tipo_terapia_create'),
    path('actualizar-tipo-terapia/<int:pk>/', login_required(TipoTerapiaActualizar.as_view()), name='tipo_terapia_update'),
    path('eliminar-tipo-terapia/<int:pk>/', login_required(TipoTerapiaEliminar.as_view()), name='tipo_terapia_delete'),
    # Donacion
    path('lista-donacion', login_required(DonacionLista.as_view()), name='donacion_list'),
    path('crear-donacion', login_required(DonacionCreate.as_view()), name='donacion_create'),
    path('actualizar-donacion/<int:pk>/', login_required(DonacionActualizar.as_view()), name='donacion_update'),
    path('eliminar-donacion/<int:pk>/', login_required(DonacionEliminar.as_view()), name='donacion_delete'),
    # Tipo Donacion
    path('lista-tipo-donacion', login_required(TipoDonacionLista.as_view()), name='tipo_donacion_list'),
    path('crear-tipo-donacion', login_required(TipoDonacionCreate.as_view()), name='tipo_donacion_create'),
    path('actualizar-tipo-donacion/<int:pk>/', login_required(TipoDonacionActualizar.as_view()), name='tipo_donacion_update'),
    path('eliminar-tipo-donacion/<int:pk>/', login_required(TipoDonacionEliminar.as_view()), name='tipo_donacion_delete'),
    # Tipo Curso
    path('lista-curso', login_required(CursoLista.as_view()), name='curso_list'),
    path('crear-curso', login_required(CursoCreate.as_view()), name='curso_create'),
    path('actualizar-curso/<int:pk>/', login_required(CursoActualizar.as_view()), name='curso_update'),
    path('eliminar-curso/<int:pk>/', login_required(CursoEliminar.as_view()), name='curso_delete'),
    # Asignación
    path('lista-asignacion', login_required(AsignacionLista.as_view()), name='asignacion_list'),
    path('crear-asignacion', login_required(AsignacionCreate.as_view()), name='asignacion_create'),
    path('actualizar-asignacion/<int:pk>/', login_required(AsignacionActualizar.as_view()), name='asignacion_update'),
    path('eliminar-asignacion/<int:pk>/', login_required(AsignacionEliminar.as_view()), name='asignacion_delete'),
    # Nota
    path('lista-nota', login_required(NotaLista.as_view()), name='nota_list'),
    path('crear-nota', login_required(NotaCreate.as_view()), name='nota_create'),
    path('actualizar-nota/<int:pk>/', login_required(NotaActualizar.as_view()), name='nota_update'),
    path('eliminar-nota/<int:pk>/', login_required(NotaEliminar.as_view()), name='nota_delete'),
    # Unidad
    path('lista-unidad', login_required(UnidadLista.as_view()), name='unidad_list'),
    path('crear-unidad', login_required(UnidadCreate.as_view()), name='unidad_create'),
    path('actualizar-unidad/<int:pk>/', login_required(UnidadActualizar.as_view()), name='unidad_update'),
    path('eliminar-unidad/<int:pk>/', login_required(UnidadEliminar.as_view()), name='unidad_delete'),                          
    # Reporte
    path('reporte-personas', login_required(generar_pdf_personas), name='reporte_personas'),
    path('reporte-notas', login_required(generar_pdf_notas), name='reporte_notas'),
]