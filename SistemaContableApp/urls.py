from django.urls  import path,include,re_path
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from django.conf import settings
from django.urls  import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.user_login, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Inicio/', views.index, name='home'),
    path('registro/', views.registration, name='registration'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('exteriorPaymentForm/', views.createExteriorPaymentForm, name = "viewExteriorPaymentForm"),
    path('chargeAccountForm/', views.createChargeAccountForm, name = "viewChargeAccountForm"),
    path('requisitionForm/', views.createRequisitionForm, name = "viewRequisitionForm"),
    path('Ventanilla única resumida/', views.summaryOneStopShopView,name = "summaryOneStopShop"),
    path('Ventanilla unica/', views.fullOneStopShopView,name = "fullOneStopShop"),
    path('Agregar a ventanilla única/', views.oneStopShopFormView,name = "OneStopShopForm"),
    path('update_state/edit/<int:following_id>', views.updateState, name='update_state'),   
    path('historial/<int:following_id>/', views.changeHistory, name='changeHistory'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/edit/', views.edit_user, name='edit_user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
]

urlpatterns += [ 
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root': settings.MEDIA_ROOT,
    })
]