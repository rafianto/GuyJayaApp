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

    @classmethod
    def sales_summary_this_month(cls):
        today = datetime.date.today()
        first_day = today.replace(day=1)
        return cls.objects.filter(
            tgl_jual__gte=first_day,
            tgl_jual__lte=today,
            status='confirmed'
        ).aggregate(
            total_sales=Sum('harga'),
            total_quantity=Sum('qty'),
            transaction_count=Count('id')
        )

    @classmethod
    def sales_by_status(cls):
        return cls.objects.values('status').annotate(
            count=Count('id'),
            total=Sum('harga')
        ).order_by('-total')

    @classmethod
    def monthly_sales_data(cls, months=12):
        result = cls.objects.filter(
            status='confirmed',
            tgl_jual__gte=datetime.date.today() - datetime.timedelta(days=30*months)
        ).annotate(
            month=models.functions.TruncMonth('tgl_jual')
        ).values('month').annotate(
            total=Sum('harga'),
            count=Count('id')
        ).order_by('month')
        
        return result

    @classmethod
    def top_selling_items(cls, limit=5):
        return cls.objects.filter(status='confirmed').values('item_barang').annotate(
            total_sales=Sum('harga'),
            total_quantity=Sum('qty')
        ).order_by('-total_sales')[:limit]
    
