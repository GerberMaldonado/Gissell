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
from django.contrib import admin
from django.urls import include, path
from .views import IndexView, PersonaLista, PersonaCreate, PersonaActualizar, PersonaEliminar
from .views import TipoPersonaLista, TipoPersonaCreate, TipoPersonaActualizar, TipoPersonaEliminar
from .views import TipoPersonaPersonaLista, TipoPersonaPersonaCreate, TipoPersonaPersonaActualizar, TipoPersonaPersonaEliminar

app_name = 'Admin'

urlpatterns = [
    path('', IndexView.as_view(), name='Home'),
    # Persona
    path('lista-persona', PersonaLista.as_view(), name='persona_list'),
    path('crear-persona', PersonaCreate.as_view(), name='persona_create'),
    path('actualizar-persona/<int:pk>/', PersonaActualizar.as_view(), name='persona_update'),
    path('eliminar-persona/<int:pk>/', PersonaEliminar.as_view(), name='persona_delete'),
    # Tipo Persona
    path('lista-tipo-persona', TipoPersonaLista.as_view(), name='tipo_persona_list'),
    path('crear-tipo-persona', TipoPersonaCreate.as_view(), name='tipo_persona_create'),
    path('actualizar-tipo-persona/<int:pk>/', TipoPersonaActualizar.as_view(), name='tipo_persona_update'),
    path('eliminar-tipo-persona/<int:pk>/', TipoPersonaEliminar.as_view(), name='tipo_persona_delete'),
    # Tipo Persona Persona
    path('lista-tipo-persona-persona', TipoPersonaPersonaLista.as_view(), name='tipo_persona_persona_list'),
    path('crear-tipo-persona-persona', TipoPersonaPersonaCreate.as_view(), name='tipo_persona_persona_create'),
    path('actualizar-tipo-persona/persona/<int:pk>/', TipoPersonaPersonaActualizar.as_view(), name='tipo_persona_persona_update'),
    path('eliminar-tipo-persona/persona/<int:pk>/', TipoPersonaPersonaEliminar.as_view(), name='tipo_persona_persona_delete'),
]