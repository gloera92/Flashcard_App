from django.db import models

# Create your models here.


class Flashcard(models.Model):
    flashcard = models.CharField(max_length=50)

    def __str__(self):
        return self.flashcard


class Collections(models.Model):
    collections = models.CharField(max_length=50)

    def __str__(self):
        return self.collections
