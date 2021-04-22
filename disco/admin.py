from django.contrib import admin
from .models import *

class MusicasAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'segundos', 'album']


admin.site.register(Musica, MusicasAdmin)
admin.site.register(Banda)
admin.site.register(Album)