from rest_framework import serializers

from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    """Serializer for the book objects"""

    class Meta:
        model = Book
        fields = (
                'id', 'title', 'authors', 
                'publisher', 'publication_date',
                'number_of_pages'
        )
        read_only_fields = ('id',)

