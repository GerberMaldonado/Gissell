# Generated by Django 2.2.6 on 2019-10-19 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=75)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('modificar', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDonacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_donacion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_persona', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoTerapia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_terapia', models.CharField(max_length=50)),
                ('sesiones', models.CharField(max_length=50)),
                ('avances', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPersonaPersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Persona')),
                ('tipo_persona_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.TipoPersona')),
            ],
        ),
        migrations.CreateModel(
            name='Terapia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_persona_persona_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.TipoPersonaPersona')),
                ('tipo_terapia_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.TipoTerapia')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.CharField(max_length=50)),
                ('tipo_persona_persona_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.TipoPersonaPersona')),
                ('unidad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Unidad')),
            ],
        ),
        migrations.CreateModel(
            name='Donacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.CharField(max_length=50)),
                ('tipo_donacion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.TipoDonacion')),
                ('tipo_persona_persona_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.TipoPersonaPersona')),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Curso')),
                ('tipo_persona_persona_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.TipoPersonaPersona')),
            ],
        ),
    ]
