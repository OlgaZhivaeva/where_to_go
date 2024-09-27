import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
from time import sleep

from places.models import Place, Image


class Command(BaseCommand):
    help = "Загружает данные в базу данных"

    def add_arguments(self, parser):
        parser.add_argument("path_to_json", type=str, help="Путь до json файла")

    def handle(self, *args, **options):
        path_to_json = options["path_to_json"]
        response = requests.get(path_to_json)
        response.raise_for_status()
        payload = response.json()
        place, created = Place.objects.get_or_create(
            title=payload["title"],
            defaults={
                "short_description": payload["description_short"],
                "long_description": payload["description_long"],
                "lng": payload["coordinates"]["lng"],
                "lat": payload["coordinates"]["lat"],
            },
        )
        if not created:
            raise CommandError("Такая локация уже загружена")
        for number, path_to_image in enumerate(payload["imgs"], start=1):
            while True:
                try:
                    response = requests.get(path_to_image)
                    response.raise_for_status()
                    image_name = os.path.basename(path_to_image)
                    image = ContentFile(response.content, name=image_name)
                    Image.objects.create(title=place, number=number, image=image)
                    self.stdout.write(self.style.SUCCESS(f"Картинка {image_name} успешно добавленa"))
                    break
                except requests.exceptions.HTTPError:
                    self.stderr.write(self.style.ERROR(f"Код ошибки загрузки картинки {response.status_code}"))
                    break
                except requests.exceptions.ConnectionError:
                    self.stderr.write(self.style.ERROR(f"Ошибка соединения при загрузке картинки {image_name}"))
                    sleep(0.2)
                    continue
        self.stdout.write(self.style.SUCCESS(f"Место {place.title} успешно добавлено"))
