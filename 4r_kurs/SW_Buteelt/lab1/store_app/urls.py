from django.urls import path
from . import views

urlpatterns = [
    path('baraa/', views.show_baraa_form, name='show_baraa'),
]