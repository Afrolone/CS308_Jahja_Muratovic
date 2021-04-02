from django.shortcuts import render
from .models import Book
from . import serializers
from rest_framework import generics

# Create your views here.

class BookListView(generics.ListCreateAPIView):
    """Used for listing and creating Books"""
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer

class BookDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Used for handling a specific Book"""
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    lookup_url_kwarg = 'id'