from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request): 
    # print ('portfolio')
    return HttpResponse("portfolio home page")

def contact(request):
    return HttpRequest("Contact me")

def greet_by_name(request, name):
    return HttpResponse(f"Hello {name}!")



