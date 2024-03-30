from django.urls  import path,include
from django.contrib import admin
from django.conf import settings
from django.urls  import path 
from . import views

urlpatterns = [
    path('', views.login, name='login_redirect'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('home/', views.index, name='home'),
    path('exteriorPaymentForm/', views.createExteriorPaymentForm, name = "viewExteriorPaymentForm"),
    path('chargeAccountForm/', views.createChargeAccountForm, name = "viewChargeAccountForm"),
    path('requisitionForm/', views.createRequisitionForm, name = "viewRequisitionForm"),
]