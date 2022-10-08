from app.models import Feature
from django.shortcuts import render
from .models import Feature


# Create your views here.
def index(request):
    return render(request,"index.html")




