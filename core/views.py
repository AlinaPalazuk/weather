import requests
from django.conf import settings
from django.shortcuts import render


def get_weather(request):

    url = 'https://community-open-weather-map.p.rapidapi.com/find'

    querystring = {
        'q': 'Tbilisi',
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
    place = data['list'][0]
    name = place['name']
    temperature = place['main']['temp']

    return render(
        request,
        'get_weather.html',
        {'name': name, 'temperature': temperature}
    )
