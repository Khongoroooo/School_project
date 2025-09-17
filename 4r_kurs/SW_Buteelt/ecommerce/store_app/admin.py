from django.contrib import admin
from .models import Angilal, Baraa

class CatAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug':('aname',)}

class BaraaAdmin (admin.ModelAdmin):
    prepopulated_fields = {'slug':('bname',)}

admin.site.register(Angilal, CatAdmin)
admin.site.register(Baraa,BaraaAdmin)


