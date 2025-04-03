from django.db import models
from kolam.models import Kolam

class IotSensor(models.Model):
    kolamdesc = models.ForeignKey(
        Kolam,
        on_delete=models.CASCADE,
        verbose_name="Kolam",
        related_name='sensor_data'
    )
    timestamp = models.DateTimeField("Waktu Pencatatan", auto_now_add=True)
    suhu = models.DecimalField("Suhu Air (°C)", max_digits=5, decimal_places=2)
    kelembaban = models.DecimalField("Kelembaban (%)", max_digits=5, decimal_places=2)
    ketinggian_air = models.DecimalField("Ketinggian Air (cm)", max_digits=5, decimal_places=2)
    ph_air = models.DecimalField("pH Air", max_digits=3, decimal_places=1)
    kualitas_air = models.CharField("Kualitas Air", max_length=20, choices=[
        ('baik', 'Baik'),
        ('sedang', 'Sedang'),
        ('buruk', 'Buruk'),
    ])
    catatan = models.TextField("Catatan Tambahan", blank=True, null=True)

    class Meta:
        verbose_name = "Data Sensor IoT"
        verbose_name_plural = "Data Sensor IoT"
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.timestamp} - {self.kolamdesc.nama_kolam}"
