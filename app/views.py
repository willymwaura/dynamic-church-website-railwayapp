from http.client import HTTPResponse
from app.models import Feature
from django.shortcuts import render
from .models import Feature
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,"index.html")
def sermons(request):
    return render(request,"sermons.html")
def events(request):
    return render(request,"events.html")
def location(request):
    return HttpResponse("<h1>good</h1>")




