from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=75)
    creacion = models.DateTimeField(auto_now_add=True)
    modificar = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s '% (self.nombre, self.apellido)

class TipoPersona(models.Model):
    tipo_persona = models.CharField(max_length=50)

class TipoPersonaPersona(models.Model):
    persona_id = models.ForeignKey(Persona, on_delete=models.CASCADE)
    tipo_persona_id = models.ForeignKey(TipoPersona, on_delete=models.CASCADE)

class TipoTerapia(models.Model):
    tipo_terapia = models.CharField(max_length=50)
    sesiones = models.CharField(max_length=50)
    avances = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

class Terapia(models.Model):
    tipo_terapia_id = models.ForeignKey(TipoTerapia, on_delete=models.CASCADE)
    tipo_persona_persona_id = models.ForeignKey(TipoPersonaPersona, on_delete=models.CASCADE)

class Curso(models.Model):
    curso = models.CharField(max_length=50)

class AsignacionCurso(models.Model):
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    tipo_persona_persona_id = models.ForeignKey(TipoPersonaPersona, on_delete=models.CASCADE)

class Unidad(models.Model):
    unidad = models.CharField(max_length=50)

class Nota(models.Model):
    nota = models.CharField(max_length=50)
    unidad_id = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    tipo_persona_persona_id = models.ForeignKey(TipoPersonaPersona, on_delete=models.CASCADE)

class TipoDonacion(models.Model):
    tipo_donacion = models.CharField(max_length=50)

class Donacion(models.Model):
    monto = models.CharField(max_length=50)
    tipo_donacion_id = models.ForeignKey(TipoDonacion, on_delete=models.CASCADE)
    tipo_persona_persona_id = models.ForeignKey(TipoPersonaPersona, on_delete=models.CASCADE)