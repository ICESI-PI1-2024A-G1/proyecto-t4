
from django.urls  import path,include
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = [

    path('', views.index), 
    path('accounts/', include('django.contrib.auth.urls')), 
    path('solicitudes/', views.solicitud)
    #path('about/', views.about),
    #path('hello/<str:username>', views.hello),
    #path('projects/', views.projects),
    #path('tasks/', views.tasks),
    #path('create_task/', views.create_task),

]