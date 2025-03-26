from django.db import models
from decimal import Decimal

class Kolam(models.Model):
    kolam_desc = models.CharField(max_length=100)
    bahan = models.CharField(max_length=50)
    diameter = models.DecimalField(max_digits=10, decimal_places=2)
    tinggi = models.DecimalField(max_digits=10, decimal_places=2)
    kapasitas = models.DecimalField(max_digits=15, decimal_places=2, editable=False)
    
    def save(self, *args, **kwargs):
        # Convert to Decimal for precise calculation
        diameter = Decimal(str(self.diameter))
        tinggi = Decimal(str(self.tinggi))
        
        # Volume calculation (πr²h) in liters
        radius = diameter / Decimal('2')
        volume_cm3 = Decimal('3.14159265359') * radius * radius * tinggi * Decimal('100')  # Convert to cm³
        self.kapasitas = volume_cm3 / Decimal('1000')  # Convert to liters
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.kolam_desc