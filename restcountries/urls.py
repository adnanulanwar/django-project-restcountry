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
    # API urls
    path('api/countries/', views.allCountries),
    path('api/listcountries/', views.countryList.as_view()),
    path('api/details/<str:name>', views.countrydetail),
    path('api/createcountry/', views.createcountry),
    path('api/update/<str:name>', views.update),
    path('api/delete/<str:name>', views.deleteCountry),
    path('api/borders/<str:name>', views.borders),
    path('api/samelang/<str:lang>', views.samelang),
    path('api/search/<str:name>', views.search),

    # URLs for template
    path('showallcountries/', views.showallcountries),
    path('view/<str:name>', views.viewcountry, name='viewcountry'),

]
