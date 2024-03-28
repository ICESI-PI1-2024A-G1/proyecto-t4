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
    

class Exterior_payment(models.Model):
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









    






