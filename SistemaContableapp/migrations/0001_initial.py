# Generated by Django 5.0.2 on 2024-03-28 20:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exterior_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiary_name', models.CharField(max_length=20)),
                ('beneficiary_last_name', models.CharField(max_length=20)),
                ('beneficiary_document_type', models.CharField(max_length=10)),
                ('beneficiary_document_no', models.CharField(max_length=20)),
                ('passport_number', models.CharField(max_length=20)),
                ('passport_expedition_city', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('bank_name', models.CharField(max_length=20)),
                ('account_type', models.CharField(choices=[('Ahorros', 'Ahorros'), ('Corriente', 'Corriente')], max_length=10)),
                ('swift_code', models.CharField(max_length=10)),
                ('iban_aba_code_type', models.CharField(choices=[('IBAN', 'IBAN'), ('ABA', 'ABA')], max_length=10)),
                ('iban_aba_code', models.CharField(max_length=10)),
                ('account_name', models.CharField(max_length=30)),
                ('account_number', models.CharField(max_length=20)),
                ('bank_address', models.TextField()),
            ],
        ),
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
