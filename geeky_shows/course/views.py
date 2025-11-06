from django.shortcuts import render, HttpResponse # type: ignore
from datetime import datetime
# Create your views here.
def course_list(req):
    return render(req, 'course/home.html')

# def learn_django(req):
#     name = 'Django'
#     duration = '4 months'
#     seats = '10'
#     course_details = {'name': name, 'duration': duration, 'seats': seats,}
#     return render(req, 'course/django.html', context=course_details)

# def learn_django(req):
#     dt = datetime.now()
#     return render(req, 'course/django.html', context={'dt': dt})


# def learn_django(req):
#     students = {'names':['Rahul', 'Sonam', 'Raj', 'Anu']}
#     return render(req, 'course/django.html', context=students)

def learn_django(req):
    return render(req, 'course/django.html',)