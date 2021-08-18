from rest_framework import serializers
from .models import RestCountry


class countrySerializer(serializers.ModelSerializer):
    class Meta:
        model = RestCountry
        fields = '__all__'
