from rest_framework import serializers
from cities.models import AlternativeName, City, Continent, Country, District, PostalCode, Region, Subregion


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ['id', 'name', 'code']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'capital', 'code3', 'population', 'area', 'currency', 'currency_name', 'phone',
                  'continent_id']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'code', 'country_id']


class SubRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subregion
        fields = ['id', 'name', 'code', 'region_id']
