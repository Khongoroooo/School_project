from .models import *

def menu_links(request):
    links = Angilal.objects.all()
    return {'links':links}