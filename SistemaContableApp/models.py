from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

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
    supports = models.FileField()


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
    
    
class Legalization(models.Model):
    """
    Model representing a legalization request.
    """
    
    BANK_ACCOUNT_TYPE =[
        ('De ahorros','De ahorros'),
        ('Corriente','Corriente')
    ]
    
    MONEY_TYPE =[
        ('PESOS COLOMBIANOS','PESOS COLOMBIANOS'),
        ('DOLARES','DOLARES'),
        ('EUROS','EUROS')
    ]

    legalization_date = models.DateField()
    traveler_name = models.CharField(max_length=50)
    identification = models.CharField(max_length = 10,default = "")
    cost_center = models.CharField(max_length = 30)
    dependency = models.CharField(max_length = 30)
    destiny_city = models.CharField(max_length = 20)
    travel_date = models.DateField()
    return_date = models.DateField()
    motive = models.TextField()
    bank = models.CharField(max_length = 20)
    type_account = models.CharField(max_length = 10,choices = BANK_ACCOUNT_TYPE)
    account_number = models.CharField(max_length = 20)
    orderer_name = models.CharField(max_length = 50)
    elaborator_name = models.CharField(max_length = 50)
    descount_in_one_quote = models.BooleanField()
    advance_payment_value = models.DecimalField(max_digits=10, decimal_places=2)
    currency_type_of_advance_value = models.CharField(max_length = 20,choices = MONEY_TYPE)
    
    def __str__(self):
        return self.id
    
class LegalizationExpense(models.Model):
    """
    Model representing a legalization expense request.
    """
    
    MONEY_TYPE =[
        ('PESOS COLOMBIANOS','PESOS COLOMBIANOS'),
        ('DOLARES','DOLARES'),
        ('EUROS','EUROS')
    ]
    solicitation = models.ForeignKey(Legalization, on_delete=models.CASCADE, related_name='expenses')
    category = models.CharField(max_length=100)
    support = models.FileField(upload_to='')
    support_no = models.CharField(max_length=20)
    third_person_name = models.CharField(max_length=100)
    third_person_nit = models.CharField(max_length=20)
    concept = models.TextField()
    money_type = models.CharField(max_length = 20,choices = MONEY_TYPE)
    money_value = models.DecimalField(max_digits=10, decimal_places=2)
    
    
class AdvancePayment(models.Model):
    """
    Model representing a advance payment request.
    """
    
    MONEY_TYPE =[
        ('PESOS COLOMBIANOS','PESOS COLOMBIANOS'),
        ('DOLARES','DOLARES'),
        ('EUROS','EUROS')
    ]
    
    radicate = models.CharField(max_length = 20)
    payment_order_code = models.CharField(max_length = 20)
    request_date = models.DateField()
    traveler_name = models.CharField(max_length=50)
    traveler_id = models.CharField(max_length = 10,default = "")  
    cost_center = models.CharField(max_length = 30)
    dependency = models.CharField(max_length = 30)
    destiny_city = models.CharField(max_length = 20)
    travel_date = models.DateField()
    return_date = models.DateField()
    motive = models.TextField()
    currency_type_of_advance_value = models.CharField(max_length = 20,choices = MONEY_TYPE)
    last_day_in_icesi = models.DateField()
    descount_in_one_quote = models.BooleanField()
    orderer_name = models.CharField(max_length = 50)
    elaborator_name = models.CharField(max_length = 50)
    
    
    def __str__(self):
        return self.id
    
class AdvanceExpense(models.Model):
    """
    Model representing a advance payment expense request.
    """

    solicitation = models.ForeignKey(AdvancePayment, on_delete=models.CASCADE, related_name='expenses')
    category = models.CharField(max_length=100)
    money_value = models.DecimalField(max_digits=10, decimal_places=2)






class State(models.Model):

    """
    Model representing the state of a following in one stop shop
    """

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
    state_history = models.ManyToManyField('State', through='StateChange', related_name='following_state_history')


    def __str__(self):
        return self.state

class Following(models.Model):

    """
    Model representing the following made to a request in one stop shop
    """

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

    state_history = models.ManyToManyField(State, through='StateChange', related_name='followings')


    def __str__(self):
        return self.type + ' - ' + self.cenco

class StateChange(models.Model):
    """
    Model representing the history of state changes for a following.
    """
    following = models.ForeignKey(Following, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    date_changed = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True) 
    


    def __str__(self):
        return f"{self.following} - {self.state} - {self.date_changed} - {self.description}"
    
class AttachedDocument(models.Model):

    """
    Model representing the doccuments attached to a following
    """

    file = models.FileField()
    associatedFollowing = models.ForeignKey(Following, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.file.name


class Rol(models.Model):
    """"
    Model definition for Rol
    """
    id= models.AutoField(primary_key= True)
    rol= models.CharField('Rol', max_length=50, unique= True)
    
    class Meta:
        """"
        Meta definition for Rol
        """
        verbose_name= 'Rol'
        verbose_name_plural= 'Rols'
        
    def _str_(self):
        """"
        Unicode representation of Rol
        """
        return self.rol
    
    
    def save(self, *args, **kwargs):
        default_permissions= ['add', 'change', 'delete', 'views']
        
        if not self.id: 
            new_group, creado= Group.objects.get_or_create(name= f'{self.rol}')
            for permission_temp in default_permissions:
                permission, created= Permission.objects.update_or_create(
                    name = f'Can {permission_temp} {self.rol}', 
                    content_type= ContentType.objects.get_for_model(Rol),
                    codename= f'{permission_temp}_{self.rol}'
                )
                if new_group:
                    new_group.permissions.add(permission.id)
            
            super().save(*args, **kwargs)
            
        else:
            ancient_role= Rol.objects.filter(id = self.id).values('rol').first()
            if ancient_role['rol'] == self.rol:
                super().save(*args, **kwargs)
            else:
                Group.objects.filter(name = ancient_role['rol']).update(name= f'{self.rol}')
                for permission_temp in default_permissions:
                    Permission.objects.filter(codename = f"{permission_temp}_{ancient_role['rol']}").update(
                        codename= f'{permission_temp}_{self.rol}',
                        name= f'Can {permission_temp} {self.rol}'
                    )
                super().save(*args, **kwargs)
   
class UserManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def _create_user(self, username, email, name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            name=name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, name, password=None, **extra_fields):
        return self._create_user(username, email, name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name, password=None, **extra_fields):
        return self._create_user(username, email, name, password, True, True, **extra_fields) 
       
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo Electrónico', unique=True, max_length=254)
    name = models.CharField('Nombre', max_length=200, blank=True, null=True)
    last_name = models.CharField('Apellidos', max_length=200, blank=True, null=True)
    rol= models.ForeignKey(Rol, on_delete=models.PROTECT, blank= True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    objects = UserManager()

    def __str__(self):
        return f'{self.name}, {self.last_name}'
    
    def save(self, *args,**kwargs):
        if not self.id:
            super().save(*args,**kwargs)
            if self.rol is not None:
                group= Group.objects.filter(name= self.rol.rol).first()
                if group:
                    self.groups.add(group)
                super().save(*args,**kwargs)
        else:
            if self.rol is not None:
                ancient_group= User.objects.filter(id= self.id).values('rol__rol').first()
                if ancient_group['rol__rol'] == self.rol.rol:
                    super().save(*args,**kwargs)
                else:
                    previous_group= Group.objects.filter(name= ancient_group['rol__rol']).first()
                    if previous_group:
                        self.groups.remove(previous_group)  
                    new_group= Group.objects.filter(name = self.rol.rol).first()
                    if new_group:
                        self.groups.add(new_group)
                    super().save(*args,**kwargs) 
                
            
    
