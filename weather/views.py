from django.shortcuts import render
import json
import urllib
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        url = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=d0d9d61a507917353f9b7fb3c397f784').read()
        json_list = json.loads(url)
        data = {
            'country_code' : str(json_list['sys']['country']),
            'coordinate' : str(json_list['coord']['lon']) + ' ' +
            str(json_list['coord']['lat']),
            'temp' : str(json_list['main']['temp']),
            'pressure' : str(json_list['main']['pressure']),
            'humidity' : str(json_list['main']['humidity']),
            'description' : str(json_list['weather'][0]['description']),
            'icon' : str(json_list['weather'][0]['icon']),
        }
    else:
        city = ''
        data = {}
    return render(request, 'index2.html',{'city':city, 'data':data})