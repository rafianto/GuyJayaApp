from django import forms # type: ignore
from decimal import Decimal  # Add this import
from .models import Kolam

class KolamForm(forms.ModelForm):
    class Meta:
        model = Kolam
        fields = '__all__'
        
    def clean_diameter(self):
        data = self.cleaned_data['diameter']
        return Decimal(str(data))
        
    def clean_tinggi(self):
        data = self.cleaned_data['tinggi']
        return Decimal(str(data))