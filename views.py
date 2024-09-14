from django.shortcuts import render
from places.models import Place, Image
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


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
                        "detailsUrl": "/static/places/moscow_legends.json"
                    }
                }
        )

    context = {
            "type": "FeatureCollection",
            "features": features
    }
    return render(request, 'index.html', context={'context': context})


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_images = place.images.all()
    response = {
        "title": place.title,
        "imgs": [place_image.image.url for place_image in place_images],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }

    return JsonResponse(response, json_dumps_params={'ensure_ascii': False, 'indent': 2})
