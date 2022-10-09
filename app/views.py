from http.client import HTTPResponse
from app.models import Event,Sermon
from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect


# Create your views here.
def index(request):
    sermons=Sermon.objects.all()

    return render(request,"index.html",{"sermons":sermons})
def home(request):
    sermons=Sermon.objects.all()

    return render(request,"index.html",{"sermons":sermons})
def sermons(request):
    sermons=Sermon.objects.all()
    return render(request,"sermons.html",{"sermons":sermons})
def events(request):
    events=Event.objects.all()
    return render(request,"events.html",{'events':events})
def location(request):
    url="https://www.google.com/maps/search/?api=1&query="
    lat=-1.095885
    long=37.040059
    ur1=url+str(lat)+"%2C"+str(long)
    return HttpResponseRedirect(ur1)




