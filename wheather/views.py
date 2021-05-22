from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# Create your views here.
def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f1deedbed88252dbe20a2fd528c2fa29&lang=tr'


    if request.method == 'POST': 
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()



        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon':  r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
        
    
    
    context = {
                'weather_data': weather_data,
                'form': form
    }
    return render(request, 'index.html', context)
