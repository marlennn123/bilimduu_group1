from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from .models import *


class CarFilter(filters.FilterSet):
    price = filters.RangeFilter(field_name='price')

    class Meta:
        model = Car
        fields = ['category', 'brand', 'model', 'price', 'city', 'country', 'volume', 'color', 'mileage']

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['model', 'brand']
    ordering_fields = ['year', 'price', 'mileage', 'volume']


# class BetFilter:
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterset_fields = []
#     search_fields = []
#     ordering_fields = []
