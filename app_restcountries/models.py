from django.db import models


class RestCountry(models.Model):
    name = models.CharField(max_length=200, default='N/A')
    alphacode2 = models.CharField(max_length=200, default='N/A')
    capital = models.CharField(max_length=200, default='N/A')
    population = models.IntegerField(default=0)
    timezone = models.TextField(default='N/A')
    flag = models.TextField(default='N/A')
    languages = models.TextField(default='N/A')
    neighbours = models.TextField(default='N/A')

    def __str__(self):
        return self.name
