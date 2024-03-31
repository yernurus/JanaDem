from . import views
from django.urls import path

urlpatterns = [
    path("home/", views.home, name = 'home'),
    path('submit_report/', views.submit_report, name='submit_report'),
    path('profile/', views.profile, name='profile'),
    path('merchandise/', views.merchandise, name='merchandise'),
    path('redeem_points/<int:merchandise_id>/', views.redeem_points, name='redeem_points'),

]