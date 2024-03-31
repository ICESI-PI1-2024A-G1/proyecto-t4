from django.db import models

#Create your models here.

class Exterior_payment(models.Model):
    """
    Model representing a exterior payment request.
    """
    
    BANK_ACCOUNT_TYPE =[
        ('Ahorros','Ahorros'),
        ('Corriente','Corriente')
    ]
    
    IBAN_ABA_CODE_TYPE =[
        ('IBAN','IBAN'),
        ('ABA','ABA')
    ]

    beneficiary_name = models.CharField(max_length = 20)
    beneficiary_last_name = models.CharField(max_length = 20)
    beneficiary_document_type = models.CharField(max_length = 10)
    beneficiary_document_no = models.CharField(max_length = 20)
    passport_number = models.CharField(max_length = 20)
    passport_expedition_city = models.CharField(max_length = 20)
    address = models.TextField()
    bank_name = models.CharField(max_length = 20)
    account_type = models.CharField(max_length = 10,choices = BANK_ACCOUNT_TYPE)
    swift_code = models.CharField(max_length = 10)
    iban_aba_code_type = models.CharField(max_length = 10, choices= IBAN_ABA_CODE_TYPE)
    iban_aba_code = models.CharField(max_length = 10)
    account_name = models.CharField(max_length = 30)
    account_number = models.CharField(max_length = 20)
    bank_address = models.TextField()



class Requisition(models.Model):
    """
    Model representing a requisition request.
    """

    BANK_ACCOUNT_TYPE =[
        ('De ahorros','De ahorros'),
        ('Corriente','Corriente')
    ]
    
    CONCEPT_OPTIONS = [
        ('Reintegro colaboradores','Reintegro colaboradores'),
        ('Patrocinio estudiantes','Patrocinio estudiantes'),
        ('Beca pasantia','Beca pasantia'),
        ('Evento de estudiantes','Evento de estudiantes'),
        ('Pago alimentación estudiante extranjero','Pago alimentación estudiante extranjero'),
        ('En la descripción','En la descripción')
    ]
    
    PAYMENT_METHOD = [
        ('Nomina','Nomina'),
        ('Consignación','Consignación')
    ]
    
    date = models.DateField()
    beneficiaryName = models.CharField(max_length = 40,default = "")
    idNumber = models.CharField(max_length = 10,default = "")
    charge = models.CharField(max_length = 40,default = "")
    dependency = models.CharField(max_length = 40,default = "")
    cenco = models.CharField(max_length = 20)
    value = models.DecimalField(decimal_places = 10,max_digits = 30)
    concept = models.CharField(max_length = 40,choices = CONCEPT_OPTIONS)
    description = models.TextField()
    radicate = models.CharField(max_length = 20)
    payment_order_code = models.CharField(max_length = 20)
    paymentMethod = models.CharField(max_length = 15,choices = PAYMENT_METHOD)
    typeAccount = models.CharField(max_length = 10,choices = BANK_ACCOUNT_TYPE)
    account_number = models.CharField(max_length = 20)
    authorName = models.CharField(max_length = 40,default = "")

    def _str_(self):
        return self.radicate



class Charge_account(models.Model):
    """
    Model representing a charge account request.
    """

    BANK_ACCOUNT_TYPE =[
        ('De ahorros','De ahorros'),
        ('Corriente','Corriente')
    ]

    name = models.CharField(max_length = 40,default = "")
    identification = models.CharField(max_length = 10,default = "")
    phone = models.CharField(max_length = 13,default = "")
    city = models.CharField(max_length = 20)
    addres = models.CharField(max_length = 50)
    date = models.DateField()
    value_letters = models.CharField(max_length = 60)
    value_numbers = models.CharField(max_length = 15)
    concept = models.TextField()
    bank = models.CharField(max_length = 20)
    type = models.CharField(max_length = 10,choices = BANK_ACCOUNT_TYPE)
    account_number = models.CharField(max_length = 20)
    cex = models.CharField(max_length = 20)
    retentions = models.BooleanField(default=False)
    declarant = models.BooleanField(default=False)
    colombian_resident = models.BooleanField(default=False)

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


class AttachedDocument(models.Model):
    file = models.FileField()
    associatedFollowing = models.ForeignKey(Following, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.file.name