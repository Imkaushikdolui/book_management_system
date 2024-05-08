from rest_framework import serializers
from .models import Book, Author, ReadingList

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'genre', 'publication_date', 'description', 'book_file']
        read_only_fields = ['id']


class ReadingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadingList
        fields = ['id', 'name', 'owner', 'books']
        read_only_fields = ['id', 'owner']

    def create(self, validated_data):
        books = validated_data.pop('books',[])
        reading_list = ReadingList.objects.create(owner=self.context['request'].user, **validated_data)
        reading_list.books.set(books)
        return reading_list