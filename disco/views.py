from django.shortcuts import render, redirect
from .models import Banda, Album, Musica
from .forms import MusicaForm
from django.core.paginator import Paginator

# C
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


# R
def getAllMusics(request):
    musicas = Musica.objects.all().order_by('-segundos')
    albuns = Album.objects.all()
    bandas = Banda.objects.all()

    # paginação
    paginator = Paginator(musicas, 7) # define quantidade a ser exibido
 
    page = request.GET.get('page') # verifica em qual página está
    posts = paginator.get_page(page) # mostra quais posts deve mostrar na página determinada

    template_name = "music_list.html"

    context = {
        "albuns": albuns,
        "bandas": bandas,
        "musicas": posts
    }

    return render(request, template_name, context)


# U
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


# D
def musica_delete(request, pk):
    musica = Musica.objects.get(pk=pk)
    musica.delete()
    return redirect('disco:musicas')
    