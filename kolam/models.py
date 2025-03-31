from django.db import models # type: ignore
from decimal import Decimal, getcontext
import math

class Kolam(models.Model):
    kolam_desc = models.CharField(max_length=100)
    bahan = models.CharField(max_length=50)
    diameter = models.DecimalField(max_digits=10, decimal_places=2)
    tinggi = models.DecimalField(max_digits=10, decimal_places=2)
    kapasitas = models.DecimalField(max_digits=15, decimal_places=2, editable=False)
    
def save(self, *args, **kwargs):
    # Validasi input
    if self.diameter is None or self.tinggi is None or self.diameter <= 0 or self.tinggi <= 0:
        raise ValueError("Diameter dan tinggi harus bernilai positif")
    
    getcontext().prec = 12
    pi = Decimal(math.pi).quantize(Decimal('1.000000000000'))
    
    # Dalam meter
    diameter = Decimal(str(self.diameter))
    tinggi = Decimal(str(self.tinggi))
    
    # Hitung volume dalam m³ dan liter
    volume_m3 = pi * ((diameter/Decimal('2')) ** 2) * tinggi
    volume_liter = volume_m3 * Decimal('1000')
    
    # Simpan kedua nilai jika diperlukan
    self.volume_m3 = volume_m3.quantize(Decimal('0.000000'))
    self.kapasitas = volume_liter.quantize(Decimal('0.000'))
    
    super().save(*args, **kwargs)

    
    def __str__(self):
        return self.kolam_desc