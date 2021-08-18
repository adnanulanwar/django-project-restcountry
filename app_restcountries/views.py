from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RestCountry
from .serializers import countrySerializer
from rest_framework.decorators import api_view


def allCountries(request):
    RestCountry.objects.all().delete()
    countries = requests.get("https://restcountries.eu/rest/v2/all").json()
    for country in countries:
        x = RestCountry()
        x.name = country['name']
        x.alphacode2 = country['alpha2Code']
        x.capital = country['capital']
        x.population = country['population']
        x.timezone = country['timezones']
        x.flag = country['flag']
        x.languages = country['languages']
        x.neighbours = country['borders']
        x.save()
    return Response("ok. data saved")


class countryList(APIView):

    def get(self, request):
        countries = RestCountry.objects.all()
        list = countrySerializer(countries, many=True)
        return Response(list.data)
