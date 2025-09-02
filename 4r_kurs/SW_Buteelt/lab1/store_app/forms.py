from django import forms
from .models import Baraa, Angilal

class BaraaForm(forms.ModelForm):
    class Meta:
        model = Baraa
        fields = ['bname', 'angilal', 'price']
        labels = {
            'bname': "Барааны нэр",
            'angilal': 'Ангилал',
            'price': 'Үнэ'
        }
