from django.contrib.auth.models import UserManager
from django.db import models
from datetime import datetime

from django.db.models.fields import json


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    message = models.TextField()
    # = models.DateField()


    def __str__(self):
        return self.name

class Location(models.Model):
    person = models.TextField(default=None)
    country = models.TextField(default=None)
    region = models.TextField(default=None)


    def __str__(self):
        return self.person