from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'car', CarViewSet)
router.register(r'bet', BetViewSet)

urlpatterns = [
    path('car/', include(router.urls)),
    path('bet/', include(router.urls)),
]
