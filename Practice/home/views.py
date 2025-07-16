from django.shortcuts import render, HttpResponse

from home.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.

def index(request):
    context ={
        'variable1':"this is variable",
        'variable2':"this is variable the great",

    }
    return render(request, 'index.html',context)
def about(request):
    return render(request, 'about.html')

    # return HttpResponse("this is aboutpage")
def services(request):
    return render(request, 'services.html')

    # return HttpResponse("this is servicespage")
def contact(request):
    if( request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        date = datetime.today()

        # Save the contact form data to the database
        contact = Contact(name=name, email=email, subject=subject, message=message, date=date)
        contact.save()
        messages.success(request, "Your form has been submitted.") 

    return render(request, 'contact.html')

    # return HttpResponse("this is contactspage")