from django.db import models

# Create your models here.


class Flashcard(models.Model):
    word = models.CharField(max_length=50)
    definition = models.CharField(max_length=50)

    def __str__(self):
        return self.word


class Collections(models.Model):
    collection = models.CharField(max_length=50)

    def __str__(self):
        return self.collection
