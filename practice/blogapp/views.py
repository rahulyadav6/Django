from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog(request, id):
	return HttpResponse(f"<h1>Post {id}</h1>")

def view_post(request, slug):
	return HttpResponse(f"<h1>Viewing {slug}</h1>")