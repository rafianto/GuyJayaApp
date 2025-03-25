from django.urls import path
from . import views
from .views import download_excel 

urlpatterns = [
    path('', views.penjualan_list, name='penjualan_list'),
    path('<int:pk>/', views.penjualan_detail, name='penjualan_detail'),
    path('create/', views.penjualan_create, name='penjualan_create'),
    path('<int:pk>/update/', views.penjualan_update, name='penjualan_update'),
    path('<int:pk>/delete/', views.penjualan_delete, name='penjualan_delete'),
    path('download-excel/', views.download_excel, name='download_excel'),
]