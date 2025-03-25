from django.db import models
from django.utils import timezone

class Cashflow(models.Model):
    tanggal = models.DateField(default=timezone.now)
    jam = models.TimeField(default=timezone.now)
    uraian = models.CharField(max_length=255)
    kas_masuk = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    kas_keluar = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    saldo = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    
    class Meta:
        ordering = ['-tanggal', '-jam']
        verbose_name_plural = 'Cashflow'
    
    def save(self, *args, **kwargs):
        # Hitung saldo otomatis sebelum menyimpan
        last_record = Cashflow.objects.order_by('-tanggal', '-jam').first()
        last_saldo = last_record.saldo if last_record else 0
        
        self.saldo = last_saldo + self.kas_masuk - self.kas_keluar
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.tanggal} - {self.uraian}"
