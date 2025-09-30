from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def city_weather(request, city_name):
    if(city_name == "delhi"):
        return HttpResponse(f"<h1>The weather of {city_name} is hot<h1>")
    elif(city_name == "mumbai"):
        return HttpResponse(f"<h1>The weather of {city_name} is humid<h1>")
    elif(city_name == "kolkata"):
        return HttpResponse(f"<h1>The weather of {city_name} is rainy<h1>")
    else:
        return HttpResponse(f"<h1>No weather data found for {city_name}<h1>")


