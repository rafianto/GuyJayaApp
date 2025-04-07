from django.apps import AppConfig

class IotSensorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iot_sensor'
    label = 'iot_sensor_unique'  # Change to something unique