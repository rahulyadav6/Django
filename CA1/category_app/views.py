from django.shortcuts import render

# Create your views here.

def technology(request):
    return render(request, 'technology.html')

def sports(request):
    return render(request, 'sports.html')

def politics(request):
    return render(request, 'politics.html')

def entertainment(request):
    return render(request, 'entertainment.html')