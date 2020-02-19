
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.posts_home),
    path('contact/', views.contact),
]
