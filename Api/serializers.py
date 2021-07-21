from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'Title', 'Author', 'Date_Added', 'Category']
