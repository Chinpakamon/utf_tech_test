from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FoodViewSet, FoodCategoryViewSet

v1_router = DefaultRouter()

v1_router.register('foods', FoodCategoryViewSet, basename='food')
v1_router.register('goods', FoodViewSet, basename='goods')

urlpatterns = [
    path('', include(v1_router.urls)),
]
