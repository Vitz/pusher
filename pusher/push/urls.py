from django.contrib import admin
from django.urls import path, include
from .views import load_from_csv, push

urlpatterns = [
    path('add/', load_from_csv),
    path('push/', push)
]
