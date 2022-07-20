from django.shortcuts import render
from rest_framework import generics
from .models import Category, Question, Quiz
from .serializers import CategorySerializer, CategoryDetailSerializer, QuestionSerializer
from .pagination import MyPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)

class CategoryDetail(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        queryset = Quiz.objects.all()
        category = self.kwargs['category']
        return queryset.filter(category__name=category)

class QuizDetail(generics.ListAPIView):
    serializer_class = QuestionSerializer
    pagination_class = MyPagination


    def get_queryset(self):
        queryset = Question.objects.all()
        return queryset.filter(quiz__title=self.kwargs['title'])