from django.db import models


#Create your models here.

class Requisition(models.Model):

    BANK_ACCOUNT_TYPE =[
        ('saving','De ahorros'),
        ('current','Corriente')
    ]


    radicate = models.CharField(max_length = 20)
    payment_order_code = models.CharField(max_length = 20)
    date = models.DateField()
    name = models.CharField(max_length = 40,default = "")
    idNumber = models.CharField(max_length = 10,default = "")
    charge = models.CharField(max_length = 40,default = "")
    dependency = models.CharField(max_length = 40,default = "")
    cenco = models.CharField(max_length = 20)
    value = models.DecimalField(decimal_places = 10,max_digits = 20)
    concept = models.TextField()
    description = models.TextField()
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
    cost_center = models.CharField(max_length = 30, null = True)
    name = models.CharField(max_length = 40,default = "")
    identificationNumber = models.CharField(max_length = 10,default = "")
    dependency = models.CharField(max_length = 30, null = True)
    destiny = models.CharField(max_length = 20, null = True)
    travel_date = models.DateField(null = True)
    return_date = models.DateField(null = True)
    motive = models.TextField(null = True)
    value = models.IntegerField(null = True)
    employee_balance = models.IntegerField(null = True)
    icesi_balance = models.IntegerField(null = True)
    descount_in_one_quote = models.BooleanField(null = True)
    elaborator_name = models.CharField(max_length = 20,null = True)
    orderer_name = models.CharField(max_length = 20,null = True)
    bank = models.CharField(max_length = 20,null = True)
    type = models.CharField(max_length = 10,choices = BANK_ACCOUNT_TYPE,null = True)
    account_number = models.CharField(max_length = 20,null = True)




class Expense(models.Model):

    MONEY_TYPE = [
        ('USD','Dolar'),
        ('COP', 'Pesos colombianos'),
        ('EUR','Euro')
    ]

    category = models.CharField(max_length = 20)
    support_no = models.IntegerField(null = True)
    third_person_name = models.CharField(max_length = 30,null = True)
    third_person_nit = models.CharField(max_length = 20,null = True)
    concept = models.TextField(null = True)
    money = models.CharField(max_length = 10, choices = MONEY_TYPE)
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
    name = models.CharField(max_length = 40,default = "")
    identificationNumber = models.CharField(max_length = 10,default = "")
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

    name = models.CharField(max_length = 40,default = "")
    identification = models.CharField(max_length = 10,default = "")
    concept = models.TextField()
    value = models.CharField(max_length = 20)
    retention_392_401 = models.BooleanField()
    retention_383 = models.BooleanField()
    declarant = models.BooleanField()
    colombian_resident = models.BooleanField()
    city = models.CharField(max_length = 20)
    date = models.DateField()
    cex = models.CharField(max_length = 20)
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


class State(models.Model):

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
        ('aprobado', 'Aprobado'),
        ('aceptado', 'Aceptado'),
        ('Rechazado por contabilidad','Rechazado por contabilidad')
    ]
    
    state = models.CharField(max_length = 30,choices = ESTADOS, primary_key = True)
    color = models.CharField(max_length = 10,choices = COLORES)

    def __str__(self):
        return self.state

class Following(models.Model):

    creationDate = models.DateField()
    creator = models.CharField(max_length = 40, null = True)
    type = models.CharField(max_length = 20)
    supplier = models.CharField(max_length = 40, null = True)
    supplierId = models.CharField(max_length = 10, null = True)
    documentNumber = models.CharField(max_length = 10, null = True)
    manager = models.CharField(max_length = 40, null = True)
    acceptor = models.CharField(max_length = 40, null = True)
    revisor = models.CharField(max_length = 40, null = True)
    acceptanceState = models.CharField(max_length = 10, null = True)
    acceptanceDate = models.DateField(null = True)
    revisionState = models.CharField(max_length = 10, null = True)
    revision = models.CharField(max_length = 40, null = True)
    concept = models.TextField()
    supplierEmail = models.EmailField(null = True)
    moneyType = models.CharField(max_length = 10)
    amount = models.IntegerField()
    cenco = models.CharField(max_length = 20)
    cexNumber = models.CharField(max_length = 20)
    observations = models.TextField()
    revisionDate = models.DateField(null = True)
    approvalState = models.CharField(max_length = 10, null = True)
    approval = models.TextField(null = True)
    approvalDate = models.DateField(null = True)
    approvalComments = models.TextField(null = True)
    accountingReception = models.CharField(max_length = 10, null = True)
    accountingComments = models.TextField(null = True)
    accountingDate = models.DateField(null = True)
    receptor = models.CharField(max_length = 40, null = True)
    modificationDate = models.DateField(null = True)
    modifier = models.CharField(max_length = 40, null = True)
    currentState = models.ForeignKey(State, on_delete = models.PROTECT)
    closeDate = models.DateField()

    def __str__(self):
        return self.type + ' - ' + self.cenco

class AttachedDocument(models.Model):
    file = models.FileField()
    associatedFollowing = models.ForeignKey(Following, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.file.name











    






