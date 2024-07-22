from django.urls import path
from django.contrib import admin
from app import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path('login', views.login, name='login')
]
