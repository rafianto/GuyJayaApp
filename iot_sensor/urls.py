from django.urls import path
from . import views
from .views import SensorListView

urlpatterns = [
    # HTML Template View (Django Class-Based View)
    path('', views.SensorListView.as_view(), name='sensor-list'),   
    
    # API Endpoints (DRF Views)
    path('api/sensor/', views.IotSensorListCreateView.as_view(), name='iot-sensor-list'),
    path('api/sensor/<int:pk>/', views.IotSensorDetailView.as_view(), name='iot-sensor-detail'),
    path('api/iot/sensor/', views.SensorListView.as_view(), name='sensor-api'),
    path('sensor/', SensorListView.as_view(), name='sensor-api'),
]