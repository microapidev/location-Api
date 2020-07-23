from rest_framework.response import Response
from rest_framework.views import APIView
from cities.models import City, Continent, Country, District, Region, Subregion
from .serializers import CountrySerializer, RegionSerializer, ContinentSerializer, SubRegionSerializer, CitySerializer, \
    DistrictSerializer

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


class CityView(APIView):

    def get(self, request):
        city = City.objects.all()
        serializer = CitySerializer(city, many=True)
        return Response(serializer.data)


class DistrictView(APIView):

    def get(self, request):
        district = District.objects.all()
        serializer = DistrictSerializer(district, many=True)
        return Response(serializer.data)
