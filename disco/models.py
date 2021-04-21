from django.db import models


class Banda(models.Model):
    nome = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Banda'
        verbose_name_plural = 'Bandas'

    def __str__(self):
        return self.nome

class Album(models.Model):
    titulo = models.CharField('Título', max_length=100)
    banda = models.ForeignKey(Banda, on_delete=models.PROTECT, verbose_name='Banda')
    data = models.DateField('Data')

    class Meta:
        verbose_name = 'Álbum'
        verbose_name_plural = 'Álbuns'

    def __str__(self):
        return self.titulo

class Musica(models.Model):
    titulo = models.CharField('Nome', max_length=100)
    segundos = models.IntegerField('Segundos', default=0)
    album = models.ForeignKey(Album, on_delete=models.PROTECT, verbose_name='Álbum')

    class Meta:
        verbose_name = 'Música'
        verbose_name_plural = 'Músicas'

    def __str__(self):
        return self.titulo