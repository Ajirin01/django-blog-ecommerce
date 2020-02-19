
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.myaccount_home),
    path('create/', views.create_account),
    path('create_handler/', views.create_account_handler),
    path('login/', views.user_login),
    path('login_handler/', views.user_login_handler),
    path('logout/', views.user_logout),
    path('reset_password/', views.reset_password),
    path('reset_password_handler/', views.reset_password_handler),
    
]
