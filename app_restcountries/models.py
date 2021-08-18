from django.db import models


class RestCountry(models.Model):
    name = models.CharField(max_length=200, unique=True)
    alphacode2 = models.CharField(max_length=200)
    capital = models.CharField(max_length=200)
    population = models.IntegerField(default=0)
    timezone = models.TextField()
    flag = models.TextField()
    languages = models.TextField()
    neighbours = models.TextField()

    def __str__(self):
        return self.name
