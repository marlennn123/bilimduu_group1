from rest_framework.pagination import PageNumberPagination
from .models import *


class CarPagination(PageNumberPagination):
    page_size = 1
    max_page_size = 1000


class BetPagination(PageNumberPagination):
    page_size = 1
    max_page_size = 1000