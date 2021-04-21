from django.urls import path

from .views import getAllMusics, musica_new

app_name = 'disco'

urlpatterns = [
    path('musica-list/', getAllMusics, name='musicas'),
    path('nova-musica/', musica_new, name="nova-musica") 
]