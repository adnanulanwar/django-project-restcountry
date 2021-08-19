from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RestCountry
from .serializers import countrySerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


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


@api_view(('GET',))
def countrydetail(request, name):
    country = get_object_or_404(RestCountry, name=name)
    response = countrySerializer(country)
    return Response(response.data)


@api_view(('POST',))
def createcountry(request):

    response = countrySerializer(data=request.data)
    if response.is_valid():
        response.save()
        return Response("data has been saved")
    return Response(response.errors, status=404)


@api_view(('PUT',))
def update(request, name):
    country = get_object_or_404(RestCountry, name=name)
    response = countrySerializer(instance=country, data=request.data)
    if response.is_valid():
        response.save()
        return Response("data has been updated")
    return Response(response.errors, status=403)


@api_view(('DELETE',))
def deleteCountry(request, name):
    country = get_object_or_404(RestCountry, name=name)
    country.delete()

    return Response("Deleted Successfully")


@api_view(('GET',))
def borders(request, name):
    country = get_object_or_404(RestCountry, name=name)
    return Response(country.neighbours)


@api_view(('GET',))
def samelang(request, lang):
    countries = RestCountry.objects.filter(languages__contains=lang)
    list = countrySerializer(countries, many=True)
    return Response(list.data)


@api_view(('GET',))
def search(request, name):
    countries = RestCountry.objects.filter(name__contains=name)
    list = countrySerializer(countries, many=True)
    return Response(list.data)


def showallcountries(request):
    countries = RestCountry.objects.all()
    return render(request, 'countrylist.html', {'countries': countries, })
