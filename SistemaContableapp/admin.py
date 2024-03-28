from django.contrib import admin
from .models import Project, Task
from .models import *
# Register your models here.
admin.site.register(Project)
admin.site.register(Task)

#admin.site.register(Bank_Account)

admin.site.register(Exterior_payment)
