from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page!")

def hello(request):
    return HttpResponse("Hello Page")

from django.shortcuts import render

def contactview(request):
    errors = {}
    submitteddata = None
    methodused = request.method

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contactmethod = request.POST.get('contactmethod')
        message = request.POST.get('message')

        # Simple validation
        if not name:
            errors['name'] = "Name is required"
        if not email:
            errors['email'] = "Email is required"
        if not contactmethod:
            errors['contactmethod'] = "Select a contact method"
        if not message:
            errors['message'] = "Message is required"

        # If no errors, save submitted data and clear form fields
        if not errors:
            submitteddata = {
                'name': name,
                'email': email,
                'contactmethod': contactmethod,
                'message': message
            }
            # Clear the input fields
            name = email = contactmethod = message = None

    return render(request, 'form1/contactform.html', {
        'submitteddata': submitteddata,
        'errors': errors,
        'methodused': methodused
    })
