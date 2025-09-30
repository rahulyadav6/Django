from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST('task')
    Task.object.create(task = task)
    return redirect('home')
