from django.db import models
from datetime import datetime

# Create your models here.
class Sermon(models.Model):
    preacher=models.CharField(max_length=100)
    theme=models.CharField(max_length=100)
    verses=models.CharField(max_length=100)
    date_today=models.DateTimeField()
    sermon_summary=models.CharField(max_length=1000)
class Event(models.Model):
    event_name=models.CharField(max_length=100)
    event_location=models.CharField(max_length=100)
    event_date=models.DateTimeField()
    event_info=models.CharField(max_length=1000)