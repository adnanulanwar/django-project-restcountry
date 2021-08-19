from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RestCountry
from .serializers import countrySerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404,  redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser.html', {'form': UserCreationForm()})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect(showallcountries)
            except IntegrityError:
                return render(request, 'signupuser.html', {'form': UserCreationForm(), 'error': 'Username already exists'})
        else:
            return render(request, 'signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords didnt match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'loginuser.html', {'form': AuthenticationForm()})

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})

        else:
            login(request, user)
            return redirect(showallcountries)


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect(home)


@login_required
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


@login_required
@api_view(('GET',))
def countryList(self, request):
    countries = RestCountry.objects.all()
    list = countrySerializer(countries, many=True)
    return Response(list.data)


@login_required
@api_view(('GET',))
def countrydetail(request, name):
    country = get_object_or_404(RestCountry, name=name)
    response = countrySerializer(country)
    return Response(response.data)


@login_required
@api_view(('POST',))
def createcountry(request):

    response = countrySerializer(data=request.data)
    if response.is_valid():
        response.save()
        return Response("data has been saved")
    return Response(response.errors, status=404)


@login_required
@api_view(('PUT',))
def update(request, name):
    country = get_object_or_404(RestCountry, name=name)
    response = countrySerializer(instance=country, data=request.data)
    if response.is_valid():
        response.save()
        return Response("data has been updated")
    return Response(response.errors, status=403)


@login_required
@api_view(('DELETE',))
def deleteCountry(request, name):
    country = get_object_or_404(RestCountry, name=name)
    country.delete()

    return Response("Deleted Successfully")


@login_required
@api_view(('GET',))
def borders(request, name):
    country = get_object_or_404(RestCountry, name=name)
    return Response(country.neighbours)


@login_required
@api_view(('GET',))
def samelang(request, lang):
    countries = RestCountry.objects.filter(languages__contains=lang)
    list = countrySerializer(countries, many=True)
    return Response(list.data)


@login_required
@api_view(('GET',))
def search(request, name):
    countries = RestCountry.objects.filter(name__contains=name)
    list = countrySerializer(countries, many=True)
    return Response(list.data)


@login_required
def showallcountries(request):
    if request.method == "GET":
        countries = RestCountry.objects.all()
        return render(request, 'countrylist.html', {'countries': countries, })
    if request.method == "POST":
        name = request.POST['namesearch']
        countries = RestCountry.objects.filter(name__contains=name)
        return render(request, 'countrylist.html', {'countries': countries, })


@login_required
def viewcountry(request, name):
    country = get_object_or_404(RestCountry, name=name)
    #country = countrySerializer(con)
    return render(request, 'viewcountry.html', {'country': country})
