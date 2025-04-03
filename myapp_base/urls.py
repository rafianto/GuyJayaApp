from django.urls import include, path # type: ignore
from django.contrib import admin # type: ignore
from .views import home_view

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('anggota/', include('anggota.urls')),
    path('penjualan/', include('penjualan.urls')),
    path('cashflows/', include('cashflows.urls')),
    path('kolam/', include('kolam.urls')),
    path('pemeliharaan/', include('pemeliharaan.urls')),
    path('sensor/', include('iot_sensor.urls')),
    path('api/iot/', include('iot_sensor.urls')),
    path('', views.home_view, name='home'),
]
