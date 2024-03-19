from django.db import models

 #Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Task(models.Model):
     
    title = models.CharField(max_length=200)
    decription = models.TextField()
    project= models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + '-' + self.project.name
#-------------------------Tutorial---------------------------------
class Solicitud(models.Model):
    nombre_completo = models.CharField(max_length=200)
    tipo_documento = models.CharField(max_length=400)
    proveedor = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo_solicitud = models.CharField(max_length=400)
    archivos_adjuntos = models.FileField(upload_to='archivos_solicitud/')

#--------------------------Project-------------------------------
    
class User(models.Model):

    name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    identification = models.CharField(max_length = 10)
    password = models.CharField(max_length = 20)
    email = models.EmailField()

    def __str__(self):
        return self.name 

class Requisition(models.Model):

    BANK_ACCOUNT_TYPE =[
        ('saving','De ahorros'),
        ('current','Corriente')
    ]


    radicate = models.CharField(max_length = 20)
    payment_order_code = models.CharField(max_length = 20)
    date = models.DateField()
    cenco = models.CharField(max_length = 20)
    value = models.DecimalField(decimal_places = 10,max_digits = 20)
    concept = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    bank = models.CharField(max_length = 20)
    type = models.CharField(max_length = 10,choices = BANK_ACCOUNT_TYPE)
    account_number = models.CharField(max_length = 20)

    def __str__(self):
        return self.radicate


class Legalization(models.Model):

    BANK_ACCOUNT_TYPE =[
        ('saving','De ahorros'),
        ('current','Corriente')
    ]

    legalization_date = models.DateField()
    cost_center = models.CharField(max_length = 30)
    dependency = models.CharField(max_length = 30)
    destiny = models.CharField(max_length = 20)
    travel_date = models.DateField()
    return_date = models.DateField()
    motive = models.TextField()
    value = models.IntegerField()
    employee_balance = models.IntegerField()
    icesi_balance = models.IntegerField()
    descount_in_one_quote = models.BooleanField()
    elaborator_name = models.CharField(max_length = 20)
    orderer_name = models.CharField(max_length = 20)
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    bank = models.CharField(max_length = 20)
    type = models.CharField(max_length = 10,choices = BANK_ACCOUNT_TYPE)
    account_number = models.CharField(max_length = 20)

    def __str__(self):
        return self.legalization_date + ' - ' + self.user



class Expense(models.Model):
    category = models.CharField(max_length = 20)
    support_no = models.IntegerField()
    third_person_name = models.CharField(max_length = 30)
    third_person_nit = models.CharField(max_length = 20)
    concept = models.TextField()
    money = models.CharField(max_length = 10)
    value = models.DecimalField(decimal_places = 10,max_digits = 20)
    legalization_facture = models.ForeignKey(Legalization, on_delete = models.CASCADE)


class Advance(models.Model):

    BANK_ACCOUNT_TYPE =[
        ('saving','De ahorros'),
        ('current','Corriente')
    ]

    radicate = models.CharField(max_length = 20)
    payment_order_code = models.CharField(max_length = 20)
    date = models.DateField()
    cost_center = models.CharField(max_length = 20)
    dependency = models.CharField(max_length = 30)
    destiny_city = models.CharField(max_length = 30)
    travel_date = models.DateField()
    return_date = models.DateField()
    motive = models.TextField()
    foreign_money = models.BooleanField()
    money = models.CharField(max_length = 10)
    last_day_at_icesi = models.DateField()
    elaborator_name = models.CharField(max_length = 20)
    orderer_name = models.CharField(max_length = 20)
    value = models.DecimalField
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    bank = models.CharField(max_length = 20)
    type = models.CharField(max_length = 10,choices = BANK_ACCOUNT_TYPE)
    account_number = models.CharField(max_length = 20)


class Expense_balance(models.Model):

    name = models.CharField(max_length = 20)
    value = models.DecimalField(decimal_places = 10,max_digits = 20)
    advance = models.ForeignKey(Advance, on_delete = models.CASCADE)


class Charge_account(models.Model):

    BANK_ACCOUNT_TYPE =[
        ('saving','De ahorros'),
        ('current','Corriente')
    ]

    concept = models.TextField()
    value = models.CharField(max_length = 20)
    retention_392_401 = models.BooleanField()
    retention_383 = models.BooleanField()
    declarant = models.BooleanField()
    colombian_resident = models.BooleanField()
    city = models.CharField(max_length = 20)
    date = models.DateField()
    cex = models.CharField(max_length = 20)
    user = models.ForeignKey(User, on_delete = models.PROTECT)
    bank = models.CharField(max_length = 20)
    type = models.CharField(max_length = 10,choices = BANK_ACCOUNT_TYPE)
    account_number = models.CharField(max_length = 20)


class Exterior_payment(models.Model):

    beneficiary_name = models.CharField(max_length = 20)
    beneficiary_last_name = models.CharField(max_length = 20)
    beneficiary_document_type = models.CharField(max_length = 10)
    beneficiary_document_no = models.CharField(max_length = 20)
    passport_number = models.CharField(max_length = 20)
    passport_expedition_city = models.CharField(max_length = 20)
    address = models.TextField()
    bank_name = models.CharField(max_length = 20)
    account_type = models.CharField(max_length = 10)
    swift_code = models.CharField(max_length = 10)
    iban_aba_code_type = models.CharField(max_length = 10)
    iban_aba_code = models.CharField(max_length = 10)
    account_name = models.CharField(max_length = 30)
    account_number = models.CharField(max_length = 20)
    bank_address = models.TextField()


class Following(models.Model):

    COLORES = [
        ('gray','Gris'),
        ('orange','Naranja'),
        ('yellow','Amarillo'),
        ('green','Verde'),
        ('blue','Azul'),
        ('red','Rojo')

    ]

    ESTADOS = [
        ('pendiente de aceptación', 'Pendiente de aceptación'),
        ('en revisión', 'En revisión'),
        ('revisado', 'Revisado'),
        ('aprovado', 'Aprobado'),
        ('aceptado', 'Aceptado'),
        ('Rechazado por contabilidad','Rechazado por contabilidad')
    ]


    state = models.CharField(max_length = 30,choices = ESTADOS)
    color = models.CharField(max_length = 10,choices = COLORES)
    creation_date = models.DateField()
    type = models.CharField(max_length = 20)
    concept = models.TextField()
    money_type = models.CharField(max_length = 10)
    amount = models.IntegerField()
    cenco = models.CharField(max_length = 20)
    cex_number = models.CharField(max_length = 20)
    observations = models.TextField()
    manager = models.ForeignKey(User, on_delete = models.PROTECT)
    close_date = models.DateField()
    
    #revisor = models.ForeignKey(User, on_delete = models.PROTECT)
    #aprover = models.ForeignKey(User, on_delete = models.PROTECT) 

    def __str__(self):
        return self.type + ' - ' + self.cenco


class Audit(models.Model):

    date = models.DateField()
    comments = models.TextField()
    assigned_request = models.ForeignKey(Following, on_delete = models.CASCADE)
    responsible = models.ForeignKey(User, on_delete = models.PROTECT)








    






