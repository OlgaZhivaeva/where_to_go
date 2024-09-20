import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Загружает данные в базу данных'

    def add_arguments(self, parser):
        parser.add_argument('path_to_json', type=str, help='Путь до json файла')

    def handle(self, *args, **options):
        path_to_json = options['path_to_json']
        response = requests.get(path_to_json)
        response.raise_for_status()
        place_data = response.json()
        place, created = Place.objects.get_or_create(
            title=place_data["title"],
            defaults={
                "description_short": place_data["description_short"],
                "description_long": place_data["description_long"],
                "lng": place_data['coordinates']["lng"],
                "lat": place_data['coordinates']["lat"],
            },
        )
        if not created:
            raise CommandError('Такая локация уже загружена')
        for number, path_to_image in enumerate(place_data['imgs'], start=1):
            response = requests.get(path_to_image)
            response.raise_for_status()
            image_name = os.path.basename(path_to_image)
            image = ContentFile(response.content, name=image_name)
            Image.objects.create(title=place, number=number, image=image)
            self.stdout.write(self.style.SUCCESS(f'Картинка {image_name} успешно добавленa'))
        self.stdout.write(self.style.SUCCESS(f'Место {place.title} успешно добавлено'))
