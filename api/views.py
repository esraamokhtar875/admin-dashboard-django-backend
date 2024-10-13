from django.shortcuts import render
from rest_framework import viewsets
from .models import Food, Category, UserProfile
from .serializers import FoodSerializer, CategorySerializer, UserProfileSerializer
from django.http import JsonResponse
from django.db.models import Q




class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


# Food Search
def food_search(request):
    query = request.GET.get('q', '')  # Get search query from the request
    if query:
        # Search for food items whose name contains the search query
        results = Food.objects.filter(Q(name__icontains=query))
    else:
        results = Food.objects.all()  # If no query, return all items
    data = list(results.values())  # Convert QuerySet to a list of dictionaries
    return JsonResponse(data, safe=False)

# Category Search
def category_search(request):
    query = request.GET.get('q', '')
    if query:
        results = Category.objects.filter(Q(name__icontains=query))
    else:
        results = Category.objects.all()
    data = list(results.values())
    return JsonResponse(data, safe=False)

# User Search
def user_search(request):
    query = request.GET.get('q', '')
    if query:
        results = UserProfile.objects.filter(Q(name__icontains=query))
    else:
        results = UserProfile.objects.all()
    data = list(results.values())
    return JsonResponse(data, safe=False)
