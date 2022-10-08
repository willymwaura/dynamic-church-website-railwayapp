from django.db import models
from datetime import datetime

# Create your models here.
class Feature(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=100)
    created=models.DateTimeField()