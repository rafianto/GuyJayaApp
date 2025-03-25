from django import forms
from .models import Cashflow

class CashflowForm(forms.ModelForm):
    class Meta:
        model = Cashflow
        fields = ['tanggal', 'jam', 'uraian', 'kas_masuk', 'kas_keluar']
        widgets = {
            'tanggal': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'jam': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
            'uraian': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Deskripsi transaksi'
            }),
            'kas_masuk': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0'
            }),
            'kas_keluar': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0'
            }),
        }