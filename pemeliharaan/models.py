from django.db import models
from kolam.models import Kolam  # Sesuaikan dengan lokasi model Kolam Anda

class PemeliharaanKolam(models.Model):
    kolamdesc = models.ForeignKey(
        Kolam, 
        on_delete=models.CASCADE,
        verbose_name="Kolam",
        related_name='pemeliharaan'
    )
    tanggal = models.DateField("Tanggal Pemeliharaan")
    uraian_kegiatan = models.TextField("Uraian Kegiatan")
    nilai_value = models.DecimalField(
        "Nilai/Nominal", 
        max_digits=10, 
        decimal_places=2,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pemeliharaan Kolam"
        verbose_name_plural = "Daftar Pemeliharaan Kolam"
        ordering = ['-tanggal']

    def __str__(self):
        return f"{self.tanggal} - {self.kolamdesc.nama_kolam}"