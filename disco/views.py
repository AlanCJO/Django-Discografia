from django.shortcuts import render

from .models import Banda, Album, Musica

def getAllMusics(request):
    musicas = Musica.objects.all()
    template_name = "music_list.html"

    context = {
        "musicas": musicas
    }

    return render(request, template_name, context)