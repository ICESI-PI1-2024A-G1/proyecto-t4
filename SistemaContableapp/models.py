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
    
    
    
class CollectionAccount(models.Model):
    remitente = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    identificacion = models.CharField(max_length=200)
    sumadeValorEnLetras = models.CharField(max_length=200)
    sumadeValorEnNumeros = models.CharField(max_length=200)
    concepto = models.CharField(max_length=200)
    ciudadYFecha = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    nombreDelBanco = models.CharField(max_length=200)
    tipoDeCuenta = models.CharField(max_length=200)
    NoDeCuenta = models.CharField(max_length=200)
    cexNo = models.CharField(max_length=200)



