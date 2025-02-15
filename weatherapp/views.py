from django.shortcuts import render,HttpResponse
import json
#if dont have requests then : pip install requests
import requests
# Create your views here.
def home(request):
    if request.method == 'POST':
        city=request.POST['city']
        source='https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=929fa2e39439602a20188c0a3f195520'
        list_of_data=requests.get(source.format(city)).json()
        data={
        "country_code": str(list_of_data['sys']['country']),
        "coordinate" : str(list_of_data['coord']['lon']) + ' ' +str(list_of_data['coord']['lat']),
        "temp" : round((list_of_data['main']['temp']))
        }
    else:
        data={}
    return render(request,'weather.html',data)
