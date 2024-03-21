from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    
    return render(request,'home.html')

def about(request):
     return render(request,'about.html')


def Course(request):
      return render(request,'course.html')
def projact(request):
      return render(request,'projact.html')
def contact(request):
      return render(request,'contact.html')
