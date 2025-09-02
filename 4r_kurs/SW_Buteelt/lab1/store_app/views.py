from django.shortcuts import render
from .forms import BaraaForm

def show_baraa_form(request):
    form = BaraaForm()
    return render (request, 'baraa.html', {'form':form})
