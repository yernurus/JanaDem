from django.contrib import admin
from django.urls import path, include
from janademApp import urls as janademApp_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('janadem/', include(janademApp_urls)),
]
