from django.shortcuts import render
from django.http import HttpResponse
from . models import Temperature

# Create your views here.

def home(request):
    temperatures = Temperature.objects.all()
    context = {
        'temperatures': temperatures 
    }
    return render(request, 'home.html', context)

def convert_temp(request, unit, value):
    try:
        temp_value = float(value)
    except ValueError:
        return HttpResponse("invalid temperature value.")
    
    result = None
    from_unit = None
    to_unit = None
    
    if unit == "c_to_f":
        result = (temp_value * 9/5) + 32
        from_unit = 'C'
        to_unit = 'F'
        response_text = f"{result:.1f}F"
        # return HttpResponse(f"{result:.1f}F")
    elif unit == "f_to_c":
        result = (temp_value - 32) * 5/9
        from_unit = 'F'
        to_unit = 'C'
        response_text = f"{result:.1f}C"
    elif unit == "c_to_k":
        result = temp_value + 273.15
        from_unit = 'C'
        to_unit = 'K'
        response_text = f"{result:.2f}K"
    elif unit == "k_to_c":
        result = temp_value - 273.15
        from_unit = 'K'
        to_unit = 'C'
        response_text = f"{result:.2f}C"
    elif unit == "f_to_k":
        celsius = (temp_value - 32) * 5/9
        result = celsius + 273.15
        from_unit = 'F'
        to_unit = 'K'
        response_text = f"{result:.2f}K"
    elif unit == "k_to_f":
        celsius = temp_value - 273.15
        result = (celsius * 9/5) + 32
        from_unit = 'K'
        to_unit = 'F'
        response_text = f"{result:.2f}F"
    else:
        return HttpResponse("Invalid unit. Use 'c_to_f', 'f_to_c', 'c_to_k', 'k_to_c', 'f_to_k', or 'k_to_f'.")
    

    Temperature.objects.create(
        value=temp_value,
        from_unit=from_unit,
        to_unit=to_unit,
        result=result
    )
    return HttpResponse(response_text)

