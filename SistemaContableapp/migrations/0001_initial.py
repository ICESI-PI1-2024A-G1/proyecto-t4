# Generated by Django 5.0.3 on 2024-03-17 04:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=200)),
                ('tipo_documento', models.CharField(max_length=400)),
                ('proveedor', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('tipo_solicitud', models.CharField(max_length=400)),
                ('archivos_adjuntos', models.FileField(upload_to='archivos_solicitud/')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('decription', models.TextField()),
                ('done', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaContableApp.project')),
            ],
        ),
    ]