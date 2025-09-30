from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def convert_temp(request, unit, value):
    try:
        temp_value = float(value)
    except ValueError:
        return HttpResponse("invalid temperature value.")
    
    if unit == "c_to_f":
        result = (temp_value * 9/5) + 32
        return HttpResponse(f"{result:.1f}F")
    elif unit == "f_to_c":
        result = (temp_value - 32) * 5/9
        return HttpResponse(f"{result:.1f}C")
    else:
        return HttpResponse("Invalid unit. Use 'c_to_f' or 'f_to_c'.")
