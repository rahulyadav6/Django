from django.shortcuts import render
from datetime import datetime, timedelta, timezone

# Create your views here.
def setsession(request):
    request.session['fname'] = 'Rahul'
    request.session['lname'] = 'Yadav'
    # request.session.set_expiry(10) #sets expiry time in seconds
    # request.session.set_expiry(0) # session expires in browser close
    return render(request, 'student/setsession.html')

def getsession(request):
    # first_name = request.session['fname']
    first_name = request.session.get('fname')
    last_name = request.session.get('lname')
    # first_name = request.session.get('fname', 'defaultValue')
    return render(request, 'student/getsession.html', {'fname': first_name, 'lname': last_name})

def delsession(request):
    if 'fname' in request.session:
        del request.session['fname']
    return render(request, 'student/delsession.html')

def flushsession(request):
    request.session.flush()
    return render(request, 'student/flushsession.html')

def sessionmethodsinview(request):
    keys = request.session.keys()
    items = request.session.items()
    print(keys)
    print(items)
    return render(request, 'student/sessionmethodsinview.html')

def clearsession(request):
    request.session.clear_expired()
    return render(request, 'student/sessionclear.html')

def sessionmethodsintemplates(request):
    keys = request.session.keys()
    items = request.session.items()
    return render(request, 'student/setsessionmethodsintemplate.html',{'keys': keys, 'items':items})