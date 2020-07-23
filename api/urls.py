from django.urls import path
from .views import CountryView, RegionView, ContinentView, SubRegionView, CityView, DistrictView


urlpatterns = [
    path('continent/', ContinentView.as_view()),
    path('country/', CountryView.as_view()),
    path('region/', RegionView.as_view()),
    path('subregion/', SubRegionView.as_view()),
    path('city/', CityView.as_view()),
    path('district/', DistrictView.as_view()),
]

