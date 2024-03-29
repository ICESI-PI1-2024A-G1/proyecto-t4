from django.db import models

 #Create your models here.

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

    def __str__(self):
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
    





