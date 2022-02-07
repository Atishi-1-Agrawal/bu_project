from django.shortcuts import render
import requests
from datetime import datetime


def index(request):

    city = request.GET.get('city' , 'Delhi')

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=619af232723df97c27d0f9fd02a9ceaf'
    data = requests.get(url).json()
    print(data)
    payload = {
    'city' : data['name'], 
    'weather' : data['weather'][0]['main'], 
    # 'icon' : data['weather'][0]['icons'], 
    'kelvin_temperature' : data['main']['temp'], 
    'min_temperature' : round(data['main']['temp_min'] - 273, ndigits=3), 
    'max_temperature' : round(data['main']['temp_max'] - 273, ndigits=3), 
    'pressure' : data['main']['pressure'], 
    'humidity' : data['main']['humidity'],
    'clouds': data['visibility'],
    'wind_speed': data['wind']['speed'],
    # 'sunset' : data['sys']['sunrise'][0:4]
    'description': data['weather'][0]['description']

    
    }

    context = {'data' : payload}
    # print(context)
    return render(request, 'weather/weather.html', context)