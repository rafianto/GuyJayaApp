from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from django.contrib import messages
from .models import PemeliharaanKolam

class PemeliharaanKolamForm(forms.ModelForm):
    class Meta:
        model = PemeliharaanKolam
        fields = '__all__'
        widgets = {
            'tanggal': forms.DateInput(attrs={'type': 'date'}),
            'uraian_kegiatan': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'kolamdesc': 'Kolam',
            'uraian_kegiatan': 'Deskripsi Kegiatan',
            'nilai_value': 'Biaya Pemeliharaan'
        }
def pemeliharaan_list(request):
    pemeliharaan_list = Pemeliharaan.objects.all().order_by('-tanggal')
    paginator = Paginator(pemeliharaan_list, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pemeliharaan/list.html', {'pemeliharaan_list': page_obj})

class PemeliharaanListView(ListView):
    model = PemeliharaanKolam
    template_name = 'pemeliharaan/list.html'
    context_object_name = 'pemeliharaan_list'
    paginate_by = 10
    ordering = ['-tanggal']  # Default ordering

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related('kolamdesc')

class PemeliharaanCreateView(CreateView):
    model = PemeliharaanKolam
    form_class = PemeliharaanKolamForm
    template_name = 'pemeliharaan/pemeliharaan_form.html'
    success_url = reverse_lazy('pemeliharaan:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Data pemeliharaan berhasil ditambahkan')
        return response

class PemeliharaanUpdateView(UpdateView):
    model = PemeliharaanKolam
    form_class = PemeliharaanKolamForm
    template_name = 'pemeliharaan/pemeliharaan_form.html'
    success_url = reverse_lazy('pemeliharaan:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Data pemeliharaan berhasil diperbarui')
        return response

class PemeliharaanDeleteView(DeleteView):
    model = PemeliharaanKolam
    template_name = 'pemeliharaan/confirm_delete.html'
    success_url = reverse_lazy('pemeliharaan:list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Data pemeliharaan berhasil dihapus")
        return super().delete(request, *args, **kwargs)