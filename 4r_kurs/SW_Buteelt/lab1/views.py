from django.shortcuts import render

def index (request):
    names = ["khongoroo","temuulen","zulaa"]
    return render (request, 'index.html', {"names":names})