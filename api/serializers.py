from rest_framework import serializers
from cities.models import Country, City, Continent, District, Region, Subregion, AlternativeName

class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name',)
        model = Continent

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'continent')
        model = Country

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'country','Region', 'subregion')
        model = City

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'country', 'code')
        model = Region

class SubregionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'code', 'region')
        model = Subregion

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'city')
        model = District

class AlternativeNameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'country')
        model = AlternativeName