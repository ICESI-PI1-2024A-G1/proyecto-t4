from django.urls  import path,include
from django.contrib import admin
from django.conf import settings
from django.urls  import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', auth_views.LoginView.as_view(), name='login'),
    path('',views.user_login, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', views.index), ###
    path('registro/', views.registration, name='registration'),
    path('contraseña/', views.olvidar_contraseña, name='olvidar_contraseña'),
    path('login/', views.user_login, name='login'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),

    
    
]