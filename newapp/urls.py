import imp
from django.urls import path
from . import views
from .views import *

app_name = 'core'

urlpatterns = [
    path('pocetna', views.pocetna, name='pocetna'),
    path('motori', views.motori, name='motori'),
]