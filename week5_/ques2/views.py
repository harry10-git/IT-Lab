from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def display(request):
    # return HttpResponse('sda')
    return render(request,'index2.html')
