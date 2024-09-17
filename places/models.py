from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('заголовок', max_length=200, unique=True)
    description_short = models.CharField('краткое описание', max_length=500)
    description_long = HTMLField('полное описание')
    lng = models.CharField('долгота', max_length=17)
    lat = models.CharField('широта', max_length=17)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = [['lng', 'lat']]
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Image(models.Model):
    title = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('картинка', db_index=True)
    number = models.PositiveIntegerField(db_index=True, editable=True, default=0)

    class Meta:
        ordering = ['number']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
