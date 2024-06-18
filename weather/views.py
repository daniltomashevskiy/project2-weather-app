from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseNotFound, HttpResponse
import json
import urllib.request



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')

# def serverError(request):
#     return HttpResponseNotFound('<h1>Server Error</h1>')
# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        if any(c.isalpha() for c in city)==True:
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city.replace(" ", "%20")+'&appid=').read()
            json_data = json.loads(res)
            data= {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ' ' +
                str(json_data['coord']['lat']),
                "temp": str(json_data['main']['temp']) + 'k',
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
            }
        else:
            city = ''
            data = {}

    return render(request, 'index.html', {'city': city, 'data': data})
