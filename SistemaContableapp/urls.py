
from django.urls  import path,include
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = [

    path('', views.login, name='login_redirect'),

    path('accounts/', include('django.contrib.auth.urls')), 
    path('base/',name = 'base.html')
 
    #path('about/', views.about),
    #path('hello/<str:username>', views.hello),
    #path('projects/', views.projects),
    #path('tasks/', views.tasks),
    #path('create_task/', views.create_task),

]