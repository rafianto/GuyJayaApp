from django import forms
from .models import PemeliharaanKolam

class PemeliharaanForm(forms.ModelForm):
    class Meta:
        model = PemeliharaanKolam
        fields = '__all__'
        widgets = {
            'tanggal': forms.DateInput(attrs={'type': 'date'}),
            'uraian_kegiatan': forms.Textarea(attrs={'rows': 3}),
        }