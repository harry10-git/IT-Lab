from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def display(request):
    # return HttpResponse('ques 4')
    return render(request,'index4.html')