from django.views.generic import ListView
from rest_framework import generics
from .models import IotSensor
from .serializers import IotSensorSerializer

# HTML Template View
class SensorListView(ListView):
    model = IotSensor
    template_name = 'iot_sensor/sensor_list.html'
    context_object_name = 'sensor_data'
    paginate_by = 10

# API Views
class IotSensorListCreateView(generics.ListCreateAPIView):
    queryset = IotSensor.objects.all()
    serializer_class = IotSensorSerializer

class IotSensorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IotSensor.objects.all()
    serializer_class = IotSensorSerializer