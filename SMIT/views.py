from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data={
        'title':'new page',

        'bdata':'this so hard langues bro',
        'number':[10,30,50,70,20],
        'ls':['php','java','python','javascript'],
        'student':[{'name':'Ali','phone':92103458},
                   {'name':'Quiser','phone':9234555543}]
    }
    return render(request,'index.html',data)

def about_us(request):
    return HttpResponse('Welcom to SMIT Programming Shop')


def Course(request):
    return HttpResponse('wlecom bro')
def courseDetails(request,courseid):
    return HttpResponse(courseid)