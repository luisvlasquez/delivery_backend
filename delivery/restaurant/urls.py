
# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter, SimpleRouter

# Views
from .views import RestaurantViewSet 

router = SimpleRouter()
router.register(r'restaurant', RestaurantViewSet ,basename='restaurant')



urlpatterns = [
    path('', include(router.urls))
]
