from django.db import models

# Create your models here.
class Anggota(models.Model):
    STATUS_CHOICES = [
        ('anggota', 'Anggota'),
        ('admin', 'Admin'),
        ('staf', 'Staf'),
    ]
    
    nik = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    tgl_lahir = models.DateField()
    tempat_lahir = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='anggota', verbose_name="Status")

    def __str__(self):
        return self.nama