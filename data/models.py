from django.db import models

# Create your models here.

class Data(models.Model):
    sname = models.CharField(max_length=100)
    sroll = models.IntegerField(max_length=5)
    scourse =  models.CharField(max_length=100)
    saddress = models.TextField()

class Contact(models.Model):
    cname = models.CharField(max_length=100)
    cemail = models.CharField(max_length=100)
    cmessage = models.TextField()
