from django.db.models import Prefetch

from rest_framework import viewsets
from .models import FoodCategory, Food
from .serializers import FoodListSerializer, FoodSerializer


class FoodCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FoodCategory.objects.filter(food__is_publish=True).prefetch_related(
        Prefetch('food', queryset=Food.objects.filter(is_publish=True)))
    # queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
