from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request): 
    # print ('portfolio')
    return HttpResponse("Portfolio Home Page")

def contact(request):
    return HttpResponse("Contact me")

def greet_by_name(request, name):
    return HttpResponse(f"Hello {name}!")



