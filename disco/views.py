from django.shortcuts import render, redirect
from .models import Banda, Album, Musica
from .forms import MusicaForm

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
        form = MusicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disco:musicas')
    else:
        template_name = 'nova_musica.html'
        context = {
            'form': MusicaForm()
        }
        return render(request, template_name, context)


def musica_edit(request, pk):
    musica = Musica.objects.get(pk=pk)
    if request.method == 'POST':
        form = MusicaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('disco:musicas')
    else:
        template_name = "editar_musica.html"
        context = {
            'form': MusicaForm(instance=musica),
            'pk': pk 
        }
        return render(request, template_name, context)


def musica_delete(request, pk):
    pass