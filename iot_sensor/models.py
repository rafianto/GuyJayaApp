
from django.db import models
from kolam.models import Kolam

class IotSensor(models.Model):
    # Simplified choices as tuples
    AIR_QUALITY_CHOICES = (
        ('baik', 'Baik'),
        ('sedang', 'Sedang'),
        ('buruk', 'Buruk'),
    )

    kolam = models.ForeignKey(
        Kolam,
        on_delete=models.CASCADE,
        related_name='sensors'
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)  # °C
    humidity = models.DecimalField(max_digits=5, decimal_places=2)     # %
    water_level = models.DecimalField(max_digits=5, decimal_places=2)  # cm
    ph_level = models.DecimalField(max_digits=3, decimal_places=1)    # pH
    water_quality = models.CharField(
        max_length=6,
        choices=AIR_QUALITY_CHOICES
    )
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "IoT Sensor Data"
        verbose_name_plural = "IoT Sensor Data"

    def __str__(self):
        return f"Sensor data for {self.kolam.nama_kolam} at {self.timestamp}"