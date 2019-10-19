from django.contrib import admin
from .models import Persona, TipoPersonaPersona, TipoPersona, TipoTerapia, Terapia 
from .models import Curso, AsignacionCurso, Unidad, Nota, TipoDonacion, Donacion
# Register your models here.

admin.site.register(Persona)
admin.site.register(TipoPersona)
admin.site.register(TipoPersonaPersona)
admin.site.register(TipoTerapia)
admin.site.register(Terapia)
admin.site.register(Curso)
admin.site.register(AsignacionCurso)
admin.site.register(Unidad)
admin.site.register(Nota)
admin.site.register(TipoDonacion)
admin.site.register(Donacion)