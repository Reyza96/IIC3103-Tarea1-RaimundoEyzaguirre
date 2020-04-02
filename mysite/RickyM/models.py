from django.db import models


class Characters(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    question_text = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=10)
    species = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    origin = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    episode = models.CharField(max_length=5000)
    url = models.CharField(max_length=200)
    created = models.CharField(max_length=200)

class Location(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    dimension = models.CharField(max_length=200)
    residents = models.CharField(max_length=5000)
    url = models.CharField(max_length=200)
    created = models.CharField(max_length=200)

class Episode(models.Model):
    id = models.CharField(primary_key=True,max_length=200)
    name = models.CharField(max_length=200)
    air_date = models.CharField(max_length=200)
    episode = models.CharField(max_length=200)
    characters = models.CharField(max_length=5000)
    url = models.CharField(max_length=200)
    created = models.CharField(max_length=200)

# Create your models here.
