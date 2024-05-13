from django.db import models

from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Service(models.Model):
    zone = models.ForeignKey(Zone, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()


class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()


