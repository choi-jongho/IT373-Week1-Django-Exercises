from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, EVSU!")

def home(request):
    return render(request, "home.html", {"title": "Home"})

def about(request):
    return render(request, "about.html", {"title": "About"})
