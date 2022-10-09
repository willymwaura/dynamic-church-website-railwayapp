
from multiprocessing import Event
from django.contrib import admin
from .models import Event, Sermon


# Register your models here.

admin.site.register(Sermon)
admin.site.register(Event)