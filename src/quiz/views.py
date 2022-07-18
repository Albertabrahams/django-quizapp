from django.shortcuts import render
from rest_framework import generics
from .models import Category, Quiz
from .serializers import CategorySerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Quiz.objects.all()
        category = self.kwargs['category']
        return queryset.filter(category__name=category)
        