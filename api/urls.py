from django.urls import path
from .views import CountryView, RegionView, ContinentView, SubRegionView


urlpatterns = [
    path('continent/', ContinentView.as_view()),
    path('country/', CountryView.as_view()),
    path('region/', RegionView.as_view()),
    path('sub_region/', SubRegionView.as_view()),
]
