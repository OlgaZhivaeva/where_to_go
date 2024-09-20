from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('заголовок', max_length=200, unique=True)
    short_description = models.TextField('краткое описание', blank=True)
    long_description = HTMLField('полное описание', blank=True)
    lng = models.FloatField('долгота')
    lat = models.FloatField('широта')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = [['lng', 'lat']]
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Image(models.Model):
    title = models.ForeignKey(Place, verbose_name='заголовок', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('картинка', db_index=True)
    number = models.PositiveIntegerField('номер', db_index=True, editable=True, default=0)

    class Meta:
        ordering = ['number']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
