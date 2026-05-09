from django import forms
from .models import Loja

class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja
        fields = ['codigo', 'cidade', 'estado', 'fase']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 117'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Joinville'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: SC'}),
            'fase': forms.Select(attrs={'class': 'form-select'}),
        }