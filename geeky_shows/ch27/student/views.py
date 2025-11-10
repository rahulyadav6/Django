from django.shortcuts import render
from student.forms import Registration, Login
from django.http import HttpResponseRedirect
from student.models import Profile
# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            city = form.cleaned_data['city']

            # print('First Name:', first_name)
            # print('Last Name:', last_name)
            # print('Email:', email)
            # print('City:', city)

            # Save data to databse
            user = Profile(First_name = first_name, Last_name = last_name, Email = email, City = city)
            user.save()


            return HttpResponseRedirect('/student/success/')
            # return HttpResponseRedirect('/student/register/')


    else:
        form = Registration()
    return render(request, 'student/registration.html', {'form': form})

def login(req):
    form = Login()
    return render(req, 'student/login.html', {'form':form})

def reg_success(req):
    return render(req, 'student/success.html')