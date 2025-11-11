from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def home(request):
    messages.add_message(request, messages.SUCCESS, 'Your account has been created')
    return render(request, 'student/home.html')

def profile(request, id):
    studentid = {'id': id}
    return render(request, 'student/profile.html', studentid)