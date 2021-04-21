from django.urls import path

from .views import getAllMusics

app_name = 'disco'

urlpatterns = [
    path('musica-list', getAllMusics, name='musicas'),
]