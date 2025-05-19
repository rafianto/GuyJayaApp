from rest_framework import serializers
from .models import IotSensor

class IotSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = IotSensor
        fields = '__all__'
        read_only_fields = ('timestamp',)

