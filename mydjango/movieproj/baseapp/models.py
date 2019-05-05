from django.db import models

# Create your models here.

class Movie(models.Model):

    year = models.IntegerField()
    rank = models.IntegerField()
    idx = models.IntegerField(primary_key=True)    #AutoField: 자동증가 메서드

    title = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    sales = models.IntegerField()
    cum_sales = models.IntegerField()
    num_audience = models.IntegerField()
    cum_audience = models.IntegerField()
    num_screen = models.IntegerField()
    showing_freq = models.IntegerField()
    nation = models.CharField(max_length=250)
    producer = models.CharField(max_length=250, null=True)
    distributor = models.CharField(max_length=250)
    grade = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    director = models.CharField(max_length=250)
    actor = models.CharField(max_length=500, null=True)
