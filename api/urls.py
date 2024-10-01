from rest_framework.routers import DefaultRouter
from .views import FoodViewSet, CategoryViewSet, UserProfileViewSet
from django.urls import path

router = DefaultRouter()
router.register(r'foods', FoodViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserProfileViewSet)

urlpatterns = router.urls

