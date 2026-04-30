from django import forms
from . import models


class InflowForm(forms.ModelForm):
        model = models.Inflow
        fields = ['supplier', 'product', 'quantity', 'description']
        widgets = {
                'supplier': forms.Select(attrs={'class': 'form-control'}),
                'product': forms.Select(attrs={'class': 'form-control', 'rows': 3}),
                'quantity': forms.NumberInput(attrs={'class': 'form-control', 'rows': 3}),
                'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
                'supplier': 'Fornecedor',
                'product': 'Produto',
                'quantity': 'Quantidade',
                'description': 'Descrição',
        }
