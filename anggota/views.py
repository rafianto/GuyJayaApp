
from django.shortcuts import render, get_object_or_404, redirect
from .models import Anggota
from django.http import HttpResponse
import pandas as pd
from django.core.paginator import Paginator


from .form import AnggotaForm  # Import the form

def anggota_update(request, id):
    anggota = get_object_or_404(Anggota, id=id)
    if request.method == 'POST':
        form = AnggotaForm(request.POST, instance=anggota)
        if form.is_valid():
            form.save()
            return redirect('anggota_list')  # Redirect to a list view or another page
    else:
        form = AnggotaForm(instance=anggota)
    return render(request, 'anggota/anggota_update.html', {'form': form})

def anggota_list(request):
    anggota_list = Anggota.objects.all()
    paginator = Paginator(anggota_list, 10)  # 10 data per halaman
    page_number = request.GET.get('page')
    anggota = paginator.get_page(page_number)
    return render(request, 'anggota/anggota_list.html', {'anggota': anggota})

def anggota_create(request):
    if request.method == "POST":
        form = AnggotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('anggota_list')
    else:
        form = AnggotaForm()
    return render(request, 'anggota/anggota_form.html', {'form': form})

def anggota_delete(request, pk):
    anggota = get_object_or_404(Anggota, pk=pk)
    if request.method == "POST":
        anggota.delete()
        return redirect('anggota_list')
    return render(request, 'anggota/anggota_confirm_delete.html', {'anggota': anggota})


def download_excel(request):
    # Ambil data dari database
    queryset = Anggota.objects.all()
    
    # Convert queryset ke DataFrame Pandas
    data = {
        "Nama": [anggota.nama for anggota in queryset],
        "NIK": [anggota.nik for anggota in queryset],
        "Alamat": [anggota.alamat for anggota in queryset],
        "Tanggal Lahir": [anggota.tgl_lahir for anggota in queryset],
        "Status": [anggota.status for anggota in queryset],
    }
    df = pd.DataFrame(data)

    # Buat file Excel dalam memory
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="daftar_anggota.xlsx"'

    # Simpan DataFrame ke Excel
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Daftar Anggota')

    return response