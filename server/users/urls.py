from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CheckAvailabilityView, ExtendedUserViewSet


router = DefaultRouter()
router.register("auth", ExtendedUserViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('check_availability/', CheckAvailabilityView.as_view())
]
