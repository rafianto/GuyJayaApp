from django.shortcuts import render # type: ignore
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .models import Kolam
from .forms import KolamForm
from django.views.generic import ListView # type: ignore
from django.contrib import messages # type: ignore

class KolamListView(ListView):
    model = Kolam
    template_name = 'kolam/kolam_list.html'
    context_object_name = 'kolam'
    paginate_by = 10

def kolam_create(request):
    if request.method == 'POST':
        form = KolamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data kolam berhasil ditambahkan!')
            return redirect('kolam_list')
    else:
        form = KolamForm()
    return render(request, 'kolam/kolam_form.html', {'form': form})

def kolam_update(request, pk):
    kolam = get_object_or_404(Kolam, pk=pk)
    if request.method == 'POST':
        form = KolamForm(request.POST, instance=kolam)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data kolam berhasil diperbarui!')
            return redirect('kolam_list')
    else:
        form = KolamForm(instance=kolam)
    return render(request, 'kolam/kolam_form.html', {'form': form, 'title': 'Edit Kolam'})

def kolam_delete(request, pk):
    kolam = get_object_or_404(Kolam, pk=pk)
    if request.method == 'POST':
        kolam.delete()
        messages.success(request, 'Data kolam berhasil dihapus!')
        return redirect('kolam_list')
    return render(request, 'kolam/kolam_confirm_delete.html', {'kolam': kolam})