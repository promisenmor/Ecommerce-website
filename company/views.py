from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('<h1> this is home.<h1>')