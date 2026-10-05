from django import forms
from .models import Loja, Computador

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

class ComputadorForm(forms.ModelForm):
    class Meta:
        model = Computador
        fields = ['hostname', 'ip', 'mac', 'processador', 'ram', 'so', 'status', 'observacoes']
        widgets = {
            'hostname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: PC-CAIXA-01'}),
            'ip': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 192.168.1.10'}),
            'mac': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: AA:BB:CC:DD:EE:FF'}),
            'processador': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Intel i5-10400'}),
            'ram': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 8'}),
            'so': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Windows 11'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Observações opcionais...'}),
        }