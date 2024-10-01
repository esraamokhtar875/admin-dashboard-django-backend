from django.shortcuts import render
from rest_framework import viewsets
from .models import Food, Category, UserProfile
from .serializers import FoodSerializer, CategorySerializer, UserProfileSerializer




class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
