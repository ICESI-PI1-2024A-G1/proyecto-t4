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
    path('exteriorPaymentForm/', views.createExteriorPaymentForm, name = "viewExteriorPaymentForm"),
    path('chargeAccountForm/', views.createChargeAccountForm, name = "viewChargeAccountForm"),
    path('requisitionForm/', views.createRequisitionForm, name = "viewRequisitionForm"),
    path('Ventanilla única resumida/', views.summaryOneStopShopView,name = "summaryOneStopShop"),
    path('Ventanilla_unica/', views.fullOneStopShopView,name = "fullOneStopShop"),
    path('Agregar a ventanilla única/', views.oneStopShopFormView,name = "OneStopShopForm"),
    path('update_state/edit/<int:following_id>', views.updateState, name='update_state'),   
    path('historial/<int:following_id>/', views.changeHistory, name='changeHistory'),
    path('approval_comment/<int:following_id>/', views.approval_comment, name='approval_comment'),
    path('accounting_comment/<int:following_id>/', views.accounting_comment, name='accounting_comment'),
    path('acceptance_state/<int:following_id>/', views.acceptance_state, name='acceptance_state'),
    path('revision_state/<int:following_id>/', views.revision_state, name='revision_state'),
    path('approval_state/<int:following_id>/', views.approval_state, name='approval_state'), 
    path('api/get-users/', get_users, name='get-users'),
    path('api/update-role/', update_role, name='update-role'),
    

]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]
