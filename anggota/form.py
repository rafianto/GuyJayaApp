from django import forms
from .models import Anggota  # Import your model

class AnggotaForm(forms.ModelForm):
    class Meta:
        model = Anggota
        fields = '__all__'
        widgets = {
            'tgl_lahir': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }        