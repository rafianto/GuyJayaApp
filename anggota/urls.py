from django.urls import include, path
from django.contrib import admin

from . import views
from .views import download_excel

urlpatterns = [
    path('', views.anggota_list, name='anggota_list'),
    path('create/', views.anggota_create, name='anggota_create'),
    path('update/<int:id>/', views.anggota_update, name='anggota_update'),
    path('delete/<int:pk>/', views.anggota_delete, name='anggota_delete'),
    path('download-excel/', views.download_excel, name='download_excel'),
]