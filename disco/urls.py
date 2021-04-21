from django.urls import path

from .views import getAllMusics, musica_new, musica_delete, musica_edit

app_name = 'disco'

urlpatterns = [
    path('musica-list/', getAllMusics, name='musicas'),
    path('nova-musica/', musica_new, name="nova-musica"),
    path('editar-musica/<int:pk>/', musica_edit, name="editar-musica")
]