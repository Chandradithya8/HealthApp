from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages

# Create your views here.

def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages.success(request, 'Form submission successful')
        return redirect('home')

    return render(request,'webpages/Contact-Us.html')
