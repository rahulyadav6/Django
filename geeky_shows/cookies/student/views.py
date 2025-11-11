from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response =  render(request, 'student/setcookie.html')
    response.set_cookie('token', 't123456', max_age=60)
    return response

def getcookie(request):
    # token = request.COOKIES['token'] #it will give error if token is not set in cookie to prevent this use below sysntax
    token = request.COOKIES.get('token', 'defaulttoken123')
    return render(request, 'student/getcookie.html', {'token':token})

def delcookie(request):
    response =  render(request, 'student/delcookie.html')
    response.delete_cookie('token')
    return response

def setsignedcookie(request):
    response = render(request, 'student/setsignedcookie.html')
    response.set_signed_cookie('token', 't123456', salt='tk',)
    return response

def getsignedcookie(request):
    token = request.get_signed_cookie('token', default="defaultsignedcookie", salt='tk')
    return render(request, 'student/getsignedcookie.html', {'token': token})