from django.db import models

class Penjualan(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]

    orderno = models.CharField(max_length=50, unique=True, verbose_name="Nomor Order", blank=True, null=True)
    tgl_jual = models.DateField(verbose_name="Tanggal Jual")
    item_barang = models.CharField(max_length=100, verbose_name="Item Barang")
    qty = models.PositiveIntegerField(verbose_name="Quantity")
    harga = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Harga")
    keterangan = models.TextField(blank=True, null=True, verbose_name="Keterangan")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name="Status")

    def __str__(self):
        return f"{self.orderno} - {self.item_barang}"

    class Meta:
        verbose_name = "Penjualan"
        verbose_name_plural = "Penjualan"
