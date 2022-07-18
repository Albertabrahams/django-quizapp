from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'quiz_count')

class CategoryDetailView(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'quiz_count')