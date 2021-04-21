from django.shortcuts import render

from .models import Banda, Album, Musica

def getAllMusics(request):
    musicas = Musica.objects.all()
    albuns = Album.objects.all()

    template_name = "music_list.html"

    context = {
        "musicas": musicas,
        "albuns": albuns

    }

    return render(request, template_name, context)

def musica_new(request):
    if request.method == 'POST':
        form 