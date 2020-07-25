import os
from rest_framework.response import Response
from rest_framework.views import APIView
from dotenv import load_dotenv
from cities.models import City, Continent, Country, District, Region, Subregion
from .serializers import CountrySerializer, RegionSerializer, ContinentSerializer, SubRegionSerializer, CitySerializer, \
    DistrictSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import status
from rest_framework_jwt.settings import api_settings

# Create your views here.

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

load_dotenv()


class ContinentView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        api_key = os.getenv('API_KEY')
        user_api_key = request.data.get('API_KEY')

        if api_key == user_api_key:
            continent = Continent.objects.all()
            serializer = ContinentSerializer(continent, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'you are not authorized to perform this action.'},
                            status=status.HTTP_401_UNAUTHORIZED)


class CountryView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        api_key = os.getenv('API_KEY')
        user_api_key = request.data.get('API_KEY')

        if api_key == user_api_key:
            country = Country.objects.all()
            serializer = CountrySerializer(country, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'you are not authorized to perform this action.'},
                            status=status.HTTP_401_UNAUTHORIZED)


class RegionView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        api_key = os.getenv('API_KEY')
        user_api_key = request.data.get('API_KEY')

        if api_key == user_api_key:
            region = Region.objects.all()
            serializer = RegionSerializer(region, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'you are not authorized to perform this action.'},
                            status=status.HTTP_401_UNAUTHORIZED)


class SubRegionView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        api_key = os.getenv('API_KEY')
        user_api_key = request.data.get('API_KEY')

        if api_key == user_api_key:
            sub_region = Subregion.objects.all()
            serializer = SubRegionSerializer(sub_region, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'you are not authorized to perform this action.'},
                            status=status.HTTP_401_UNAUTHORIZED)


class CityView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        api_key = os.getenv('API_KEY')
        user_api_key = request.data.get('API_KEY')

        if api_key == user_api_key:
            city = City.objects.all()
            serializer = CitySerializer(city, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'you are not authorized to perform this action.'},
                            status=status.HTTP_401_UNAUTHORIZED)


class DistrictView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        api_key = os.getenv('API_KEY')
        user_api_key = request.data.get('API_KEY')

        if api_key == user_api_key:
            district = District.objects.all()
            serializer = DistrictSerializer(district, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'you are not authorized to perform this action.'},
                            status=status.HTTP_401_UNAUTHORIZED)
