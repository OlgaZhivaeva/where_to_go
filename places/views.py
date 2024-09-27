from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from places.models import Place


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        features.append(
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [place.lng, place.lat]
                    },
                    "properties": {
                        "title": place.title,
                        "placeId": place.id,
                        "detailsUrl": reverse("place_detail", args=[place.id])
                    }
                }
        )

    context = {
            "type": "FeatureCollection",
            "features": features
    }
    return render(request, "index.html", context={"context": context})


def place_detail(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related("images"), id=place_id)
    place_images = place.images.all()
    response = {
        "title": place.title,
        "imgs": [place_image.image.url for place_image in place_images],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }

    return JsonResponse(response, json_dumps_params={"ensure_ascii": False, "indent": 2})
