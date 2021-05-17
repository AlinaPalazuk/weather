import requests

from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Place


def place_list(request):
    places = Place.objects.all()
    return render(request, 'place_list.html', {'places': places})


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    url = 'https://community-open-weather-map.p.rapidapi.com/find'

    querystring = {
        'q': place.name,
        'cnt': '1',
        'mode': 'null',
        'lon': '0',
        'type': 'link, accurate',
        'lat': '0',
        'units': 'metric',
    }

    headers = {
        'x-rapidapi-key': settings.RAPIDAPI_KEY,
        'x-rapidapi-host': 'community-open-weather-map.p.rapidapi.com',
    }

    response = requests.request(
        'GET', url, headers=headers, params=querystring
    )

    data = response.json()
    name = data['list'][0]['name']
    temperature = data['list'][0]['main']['temp']

    return render(
        request,
        'place_detail.html',
        {'name': name, 'temperature': temperature}
    )
