from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Penjualan
import datetime

@receiver(pre_save, sender=Penjualan)
def generate_orderno(sender, instance, **kwargs):
    if not instance.orderno:  # Jika orderno belum diisi
        # Ambil tahun saat ini
        tahun = datetime.datetime.now().strftime('%Y')
        
        # Ambil nomor urut terakhir untuk tahun ini
        last_order = Penjualan.objects.filter(orderno__startswith=tahun).order_by('-orderno').first()
        
        if last_order:
            # Ambil nomor urut terakhir dan tambahkan 1
            last_number = int(last_order.orderno.split('-')[-1])
            new_number = last_number + 1
        else:
            # Jika belum ada data untuk tahun ini, mulai dari 1
            new_number = 1
        
        # Format orderno: TAHUN-NOMORURUT (contoh: 2023-0001)
        instance.orderno = f"{tahun}-{new_number:04d}"