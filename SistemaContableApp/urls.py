from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from .views.get_users import get_users
from .views.update_role import update_role
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.user_login, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Inicio/', views.index, name='home'),
    path('registro/', views.registration, name='registration'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('exteriorPaymentForm/', views.createExteriorPaymentForm, name="viewExteriorPaymentForm"),
    path('chargeAccountForm/', views.createChargeAccountForm, name="viewChargeAccountForm"),
    path('requisitionForm/', views.createRequisitionForm, name="viewRequisitionForm"),
    path('Ventanilla_unica_resumida/', views.summaryOneStopShopView, name="summaryOneStopShop"),
    path('Ventanilla_unica/', views.fullOneStopShopView, name="fullOneStopShop"),
    path('Agregar_a_ventanilla_unica/', views.oneStopShopFormView, name="OneStopShopForm"),
    path('api/get-users/', get_users, name='get-users'),
    path('api/update-role/', update_role, name='update-role'),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]
