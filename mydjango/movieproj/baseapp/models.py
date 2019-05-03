from django.db import models

# Create your models here.
class Movie(models.Model):
    code = models.IntegerField()
    title = models.CharField(max_length=100)
    date = models.DateField()
    genre = models.CharField(max_length=100)
