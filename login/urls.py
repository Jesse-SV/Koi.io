from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view, atualizar_perfil

urlpatterns = [
    path('', login_view, name='login'),

    path('atualizar_perfil/<int:id>/',atualizar_perfil, name="atualizar_perfil"),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name= 'password_reset.html'), name='password_reset'),

    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(template_name= 'password_reset_done.html'), name='password_reset_done'),

    path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'password_reset_complete.html'), name='password_reset_complete'),
    
]
