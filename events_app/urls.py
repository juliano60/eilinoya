from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vins', views.display_wine, name='vins'),
    path('contact', views.display_contact, name='contact')
]
