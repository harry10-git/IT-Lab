from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def display(request):
    # return HttpResponse('ques 3')
    return render(request,'index3.html')