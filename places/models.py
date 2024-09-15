from django.db import models
from django.utils.html import format_html


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=500)
    description_long = models.TextField()
    lng = models.CharField(max_length=17)
    lat = models.CharField(max_length=17)


    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.ForeignKey(Place, on_delete=models.CASCADE,
                                related_name='images')
    image = models.ImageField(db_index=True)
    number = models.PositiveIntegerField()


    def __str__(self):
        return f'{self.number} {self.title}'


    class Meta:
        ordering = ['number']