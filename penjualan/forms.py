from django import forms
from .models import Penjualan

class PenjualanForm(forms.ModelForm):
    class Meta:
        model = Penjualan
        fields = '__all__'
        widgets = {
            'tgl_jual': forms.DateInput(attrs={'type': 'date'}),
            'keterangan': forms.Textarea(attrs={'rows': 3}),
        }
        exclude = ['orderno'] 

# class PenjualanForm(forms.ModelForm):
#     class Meta:
#         model = Penjualan
#         fields = '__all__'
#         widgets = {
#             'tgl_jual': forms.DateInput(attrs={'class': 'form-control datepicker'}),
#             'status': forms.Select(attrs={'class': 'form-select'}),
#             'qty': forms.NumberInput(attrs={'class': 'form-control'}),
#             'harga': forms.NumberInput(attrs={'class': 'form-control price-input'}),
#             'item_barang': forms.Select(attrs={'class': 'form-control select2'}),
#             'keterangan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#         }
#         exclude = ['orderno'] 