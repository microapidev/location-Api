from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from cities.models import AlternativeName, City, Continent, Country, District, PostalCode, Region, Subregion
from .serializers import CountrySerializer, RegionSerializer, ContinentSerializer, SubRegionSerializer

# Create your views here.


class ContinentView(APIView):

    def get(self, request):
        continent = Continent.objects.all()
        serializer = ContinentSerializer(continent, many=True)
        return Response(serializer.data)


class CountryView(APIView):

    def get(self, request):
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)


class RegionView(APIView):

    def get(self, request):
        region = Region.objects.all()
        serializer = RegionSerializer(region, many=True)
        return Response(serializer.data)


class SubRegionView(APIView):

    def get(self, request):
        sub_region = Subregion.objects.all()
        serializer = SubRegionSerializer(sub_region, many=True)
        return Response(serializer.data)
