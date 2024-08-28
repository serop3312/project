from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service/engine-repair/', views.service_engine_repair, name='service_engine_repair'),
    path('service/oil-change/', views.service_oil_change, name='service_oil_change'),
    path('service/suspension-repair/', views.service_suspension_repair, name='service_suspension_repair'),
    path('service/body-repair/', views.service_body_repair, name='service_body_repair'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]