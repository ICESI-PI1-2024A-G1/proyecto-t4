# Generated by Django 5.0.4 on 2024-05-06 07:05

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvancePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radicate', models.CharField(max_length=20)),
                ('payment_order_code', models.CharField(max_length=20)),
                ('request_date', models.DateField()),
                ('traveler_name', models.CharField(max_length=50)),
                ('traveler_id', models.CharField(default='', max_length=10)),
                ('cost_center', models.CharField(max_length=30)),
                ('dependency', models.CharField(max_length=30)),
                ('destiny_city', models.CharField(max_length=20)),
                ('travel_date', models.DateField()),
                ('return_date', models.DateField()),
                ('motive', models.TextField()),
                ('currency_type_of_advance_value', models.CharField(choices=[('PESOS COLOMBIANOS', 'PESOS COLOMBIANOS'), ('DOLARES', 'DOLARES'), ('EUROS', 'EUROS')], max_length=20)),
                ('last_day_in_icesi', models.DateField()),
                ('descount_in_one_quote', models.BooleanField()),
                ('orderer_name', models.CharField(max_length=50)),
                ('elaborator_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Charge_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('identification', models.CharField(default='', max_length=10)),
                ('phone', models.CharField(default='', max_length=13)),
                ('city', models.CharField(max_length=20)),
                ('addres', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('value_letters', models.CharField(max_length=60)),
                ('value_numbers', models.CharField(max_length=15)),
                ('concept', models.TextField()),
                ('bank', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('De ahorros', 'De ahorros'), ('Corriente', 'Corriente')], max_length=10)),
                ('account_number', models.CharField(max_length=20)),
                ('cex', models.CharField(max_length=20)),
                ('retentions', models.BooleanField(default=False)),
                ('declarant', models.BooleanField(default=False)),
                ('colombian_resident', models.BooleanField(default=False)),
                ('supports', models.FileField(upload_to='')),
            ],
        ),
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
            name='Following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creationDate', models.DateField()),
                ('creator', models.CharField(max_length=40, null=True)),
                ('type', models.CharField(max_length=20)),
                ('supplier', models.CharField(max_length=40, null=True)),
                ('supplierId', models.CharField(max_length=10, null=True)),
                ('documentNumber', models.CharField(max_length=10, null=True)),
                ('manager', models.CharField(max_length=40, null=True)),
                ('acceptor', models.CharField(max_length=40, null=True)),
                ('revisor', models.CharField(max_length=40, null=True)),
                ('acceptanceState', models.CharField(max_length=10, null=True)),
                ('acceptanceDate', models.DateField(null=True)),
                ('revisionState', models.CharField(max_length=10, null=True)),
                ('revision', models.CharField(max_length=40, null=True)),
                ('concept', models.TextField()),
                ('supplierEmail', models.EmailField(max_length=254, null=True)),
                ('moneyType', models.CharField(max_length=10)),
                ('amount', models.IntegerField()),
                ('cenco', models.CharField(max_length=20)),
                ('cexNumber', models.CharField(max_length=20)),
                ('observations', models.TextField()),
                ('revisionDate', models.DateField(null=True)),
                ('approvalState', models.CharField(max_length=10, null=True)),
                ('approval', models.TextField(null=True)),
                ('approvalDate', models.DateField(null=True)),
                ('approvalComments', models.TextField(null=True)),
                ('accountingReception', models.CharField(max_length=10, null=True)),
                ('accountingComments', models.TextField(null=True)),
                ('accountingDate', models.DateField(null=True)),
                ('receptor', models.CharField(max_length=40, null=True)),
                ('modificationDate', models.DateField(null=True)),
                ('modifier', models.CharField(max_length=40, null=True)),
                ('closeDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Legalization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legalization_date', models.DateField()),
                ('traveler_name', models.CharField(max_length=50)),
                ('identification', models.CharField(default='', max_length=10)),
                ('cost_center', models.CharField(max_length=30)),
                ('dependency', models.CharField(max_length=30)),
                ('destiny_city', models.CharField(max_length=20)),
                ('travel_date', models.DateField()),
                ('return_date', models.DateField()),
                ('motive', models.TextField()),
                ('bank', models.CharField(max_length=20)),
                ('type_account', models.CharField(choices=[('De ahorros', 'De ahorros'), ('Corriente', 'Corriente')], max_length=10)),
                ('account_number', models.CharField(max_length=20)),
                ('orderer_name', models.CharField(max_length=50)),
                ('elaborator_name', models.CharField(max_length=50)),
                ('descount_in_one_quote', models.BooleanField()),
                ('advance_payment_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency_type_of_advance_value', models.CharField(choices=[('PESOS COLOMBIANOS', 'PESOS COLOMBIANOS'), ('DOLARES', 'DOLARES'), ('EUROS', 'EUROS')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('beneficiaryName', models.CharField(default='', max_length=40)),
                ('idNumber', models.CharField(default='', max_length=10)),
                ('charge', models.CharField(default='', max_length=40)),
                ('dependency', models.CharField(default='', max_length=40)),
                ('cenco', models.CharField(max_length=20)),
                ('value', models.DecimalField(decimal_places=10, max_digits=30)),
                ('concept', models.CharField(choices=[('Reintegro colaboradores', 'Reintegro colaboradores'), ('Patrocinio estudiantes', 'Patrocinio estudiantes'), ('Beca pasantia', 'Beca pasantia'), ('Evento de estudiantes', 'Evento de estudiantes'), ('Pago alimentación estudiante extranjero', 'Pago alimentación estudiante extranjero'), ('En la descripción', 'En la descripción')], max_length=40)),
                ('description', models.TextField()),
                ('radicate', models.CharField(max_length=20)),
                ('payment_order_code', models.CharField(max_length=20)),
                ('paymentMethod', models.CharField(choices=[('Nomina', 'Nomina'), ('Consignación', 'Consignación')], max_length=15)),
                ('typeAccount', models.CharField(choices=[('De ahorros', 'De ahorros'), ('Corriente', 'Corriente')], max_length=10)),
                ('account_number', models.CharField(max_length=20)),
                ('authorName', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(max_length=50, unique=True, verbose_name='Rol')),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Rols',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state', models.CharField(choices=[('pendiente de aceptación', 'Pendiente de aceptación'), ('en revisión', 'En revisión'), ('revisado', 'Revisado'), ('aprobado', 'Aprobado'), ('aceptado', 'Aceptado'), ('Rechazado por contabilidad', 'Rechazado por contabilidad')], max_length=30, primary_key=True, serialize=False)),
                ('color', models.CharField(choices=[('gray', 'Gris'), ('orange', 'Naranja'), ('yellow', 'Amarillo'), ('green', 'Verde'), ('blue', 'Azul'), ('red', 'Rojo')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AdvanceExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('money_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('solicitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='SistemaContableApp.advancepayment')),
            ],
        ),
        migrations.CreateModel(
            name='AttachedDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('associatedFollowing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaContableApp.following')),
            ],
        ),
        migrations.CreateModel(
            name='LegalizationExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('support', models.FileField(upload_to='')),
                ('support_no', models.CharField(max_length=20)),
                ('third_person_name', models.CharField(max_length=100)),
                ('third_person_nit', models.CharField(max_length=20)),
                ('concept', models.TextField()),
                ('money_type', models.CharField(choices=[('PESOS COLOMBIANOS', 'PESOS COLOMBIANOS'), ('DOLARES', 'DOLARES'), ('EUROS', 'EUROS')], max_length=20)),
                ('money_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('solicitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='SistemaContableApp.legalization')),
            ],
        ),
        migrations.AddField(
            model_name='following',
            name='currentState',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SistemaContableApp.state'),
        ),
        migrations.CreateModel(
            name='StateChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_changed', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaContableApp.following')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SistemaContableApp.state')),
            ],
        ),
        migrations.AddField(
            model_name='state',
            name='state_history',
            field=models.ManyToManyField(related_name='following_state_history', through='SistemaContableApp.StateChange', to='SistemaContableApp.state'),
        ),
        migrations.AddField(
            model_name='following',
            name='state_history',
            field=models.ManyToManyField(related_name='followings', through='SistemaContableApp.StateChange', to='SistemaContableApp.state'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Apellidos')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('rol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='SistemaContableApp.rol')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
