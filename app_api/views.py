from django.shortcuts import render
from requests import get
from django.contrib import messages
import datetime
# Create your views here.

def index(request):
        if 'city' in request.POST:  #if request.method == 'POST':
         city = request.POST['city']
        else:
         city = 'DELHI'  
        url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=992a3811c073262fb94c694dbd7eb9de&units=metric"
        
        response = get(url)  #FETCH THE RESPONSE
    
        data = response.json() #CONVERT INTO JSON DATA
        
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        humidity = data['main']['humidity']
        temperature = data['main']['temp']
        wind_speed = data['wind']['speed']
        day = datetime.date.today()
        
        imageurl = "http://openweathermap.org/img/w/"+icon+".png" # CONVERT ICON/WEATHER CODE  INTO IMAGE
            #print(f'Icon:{imageurl}')
        
        context ={ 
            'city':city,  
            'description': description,
            'humidity': humidity,
            'temperature': temperature,
            'windspeed': wind_speed,
            'dattime' : day,
            'imageurl': imageurl,   
            }
        return render(request,'index.html',context)
        
        