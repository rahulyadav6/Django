from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task
# Create your views here.

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.isCompleted = True
    task.save()
    return redirect('home')

def mark_as_unDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.isCompleted = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        updated_task = request.POST['task']
        get_task.task = updated_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
    return render(request, 'edit_task.html', context)