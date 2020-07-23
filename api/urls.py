from rest_framework.routers import SimpleRouter

from .views import CountryViewSet, ContinentViewSet, CityViewSet, RegionViewSet, SubRegionViewSet, DistrictViewSet, AlternativeNameViewSet

router = SimpleRouter()
router.register('country', CountryViewSet, basename='country')
router.register('continent', ContinentViewSet, basename='continent')
router.register('city', CityViewSet, basename='city')
router.register('region', RegionViewSet, basename='region')
router.register('subregion', SubRegionViewSet, basename='subregion')
router.register('district', DistrictViewSet, basename='district')
router.register('alternativename', AlternativeNameViewSet, basename='alternativename')


urlpatterns = router.urls