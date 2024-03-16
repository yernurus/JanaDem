from django.contrib import admin
from django.urls import path, include
from janademApp import views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('success/', views.success, name='success_url'),
    path('registration/', views.registration, name='registration'),
    path('registration/success/', views.registration_success, name='registration_success'),
]