from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from .models import PemeliharaanKolam

# Create a ModelForm for PemeliharaanKolam
class PemeliharaanKolamForm(forms.ModelForm):
    class Meta:
        model = PemeliharaanKolam
        fields = '__all__'  # or specify fields explicitly: ['field1', 'field2', ...]

class PemeliharaanListView(ListView):
    model = PemeliharaanKolam
    template_name = 'pemeliharaan/list.html'
    context_object_name = 'list'
    paginate_by = 10

    def get_queryset(self):
        return PemeliharaanKolam.objects.select_related('kolamdesc').order_by('-id')

class PemeliharaanCreateView(CreateView):
    model = PemeliharaanKolam
    form_class = PemeliharaanKolamForm  # Use the form class instead of the model
    template_name = 'pemeliharaan/pemeliharaan_form.html'
    success_url = reverse_lazy('pemeliharaan:list')

    def form_valid(self, form):
        # Optional: Add any pre-save logic here
        return super().form_valid(form)

class PemeliharaanUpdateView(UpdateView):
    model = PemeliharaanKolam
    form_class = PemeliharaanKolamForm  # Use the form class instead of the model
    template_name = 'pemeliharaan/pemeliharaan_form.html'
    success_url = reverse_lazy('pemeliharaan:list')

class PemeliharaanDeleteView(DeleteView):
    model = PemeliharaanKolam
    template_name = 'pemeliharaan/confirm_delete.html'
    success_url = reverse_lazy('pemeliharaan:list')

    def delete(self, request, *args, **kwargs):
        from django.contrib import messages
        messages.success(self.request, "Record deleted successfully")
        return super().delete(request, *args, **kwargs)