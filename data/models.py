from django.db import models

# Create your models here.

class Data(models.Model):
    sname = models.CharField(max_length=100)
    sroll = models.IntegerField()
    scourse = models.CharField(max_length=100)
    saddress = models.TextField()

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    cname = models.CharField(max_length=100)
    cemail = models.CharField(max_length=100)
    cmessage = models.TextField()
