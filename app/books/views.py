from django.shortcuts import render
from .models import Book
from . import serializers
from rest_framework import generics

# Create your views here.

class BookListViewSet(generics.ListCreateAPIView):
    """Used for listing and creating Books"""
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer