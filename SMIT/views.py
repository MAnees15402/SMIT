from django.http import HttpResponse
from django.shortcuts import render
from new.models import contact  # Capitalize model name

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def course(request):
    return render(request, 'course.html')

def projact(request):
    return render(request, 'projact.html')

def contact(request):  # Rename the view function
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        
        # Create an instance of the Contact model and save it
        ins = contact(name=name, email=email, password=password)
        ins.save()
        print('the Data Send to DataBase')

    return render(request, 'contact.html')
