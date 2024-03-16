from django.contrib import admin
from django.urls import path, include
from janademApp import views


urlpatterns = [
    path('new/', views.login, name='new_report'),
    
]