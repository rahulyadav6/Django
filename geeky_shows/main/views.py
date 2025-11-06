from django.shortcuts import render # pyright: ignore[reportMissingModuleSource]
def homepage(req):
    return render(req, 'home.html')