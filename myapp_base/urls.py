from django.urls import include, path
from django.contrib import admin
from .views import home_view

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('anggota/', include('anggota.urls')),
    path('penjualan/', include('penjualan.urls')),
    path('cashflows/', include('cashflows.urls')),
    path('kolam/', include('kolam.urls')),
    path('', views.home_view, name='home'),
]
