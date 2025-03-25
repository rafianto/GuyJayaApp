from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Penjualan
import pandas as pd

from .forms import PenjualanForm

# List Penjualan
def penjualan_list(request):
    # Ambil semua data penjualan
    penjualan_list = Penjualan.objects.all()
    # Pagination: 10 data per halaman
    paginator = Paginator(penjualan_list, 10)
    page_number = request.GET.get('page')  # Ambil nomor halaman dari parameter URL
    penjualan = paginator.get_page(page_number)
    return render(request, 'penjualan/penjualan_list.html', {'penjualan': penjualan})

# Detail Penjualan
def penjualan_detail(request, pk):
    penjualan = get_object_or_404(Penjualan, pk=pk)
    return render(request, 'penjualan/penjualan_detail.html', {'penjualan': penjualan})

# Tambah Penjualan
def penjualan_create(request):
    if request.method == 'POST':
        form = PenjualanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('penjualan_list')
    else:
        form = PenjualanForm()
    return render(request, 'penjualan/penjualan_form.html', {'form': form})

# Edit Penjualan
def penjualan_update(request, pk):
    penjualan = get_object_or_404(Penjualan, pk=pk)
    if request.method == 'POST':
        form = PenjualanForm(request.POST, instance=penjualan)
        if form.is_valid():
            form.save()
            return redirect('penjualan_list')
    else:
        form = PenjualanForm(instance=penjualan)
    return render(request, 'penjualan/penjualan_form.html', {'form': form})

# Hapus Penjualan
def penjualan_delete(request, pk):
    penjualan = get_object_or_404(Penjualan, pk=pk)
    if request.method == 'POST':
        penjualan.delete()
        return redirect('penjualan_list')
    return render(request, 'penjualan/penjualan_confirm_delete.html', {'penjualan': penjualan})

def download_excel(request):
    # Ambil data dari database
    queryset = Penjualan.objects.all()
    
    # Konversi queryset ke DataFrame
    data = {
        'No. Order': [p.orderno for p in queryset],
        'Tanggal Jual': [p.tgl_jual for p in queryset],
        'Item Barang': [p.item_barang for p in queryset],
        'Qty': [p.qty for p in queryset],
        'Harga': [p.harga for p in queryset],
        'Keterangan': [p.keterangan for p in queryset],
        'Status': [p.status for p in queryset],
    }
    df = pd.DataFrame(data)
    
    # Buat response dengan file Excel
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="daftar_penjualan.xlsx"'
    
    # Simpan DataFrame ke Excel
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Daftar Penjualan')
    
    return response
