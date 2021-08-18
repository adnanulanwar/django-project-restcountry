"""restcountries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_restcountries import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('countries/', views.allCountries),
    path('listcountries/', views.countryList.as_view()),
    path('details/<str:name>', views.countrydetail),
    path('createcountry/', views.createcountry),
    path('update/<str:name>', views.update),
    path('delete/<str:name>', views.deleteCountry),
    path('borders/<str:name>', views.borders),
    path('samelang/<str:lang>', views.samelang),
    path('search/<str:name>', views.search),
]
