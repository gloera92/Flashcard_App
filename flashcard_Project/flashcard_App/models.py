from django.db import models

# Create your models here.


class Flashcard(models.Model):
    word = models.CharField(max_length=50, default=None)
    definition = models.CharField(max_length=500, default=None)


class Collections(models.Model):
    collection = models.CharField(max_length=50, default=None)

