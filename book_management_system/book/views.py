from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Author, ReadingList
from .serializers import BookSerializer, AuthorSerializer, ReadingListSerializer
from django.http import Http404


# Author related API's
class AuthorCreateAPIView(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorUpdateAPIView(APIView):
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorDeleteAPIView(APIView):
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        author = self.get_object(pk)
        if author:
            author.delete()
            return Response({"Message":"Author deleted successfully"},status= 204)
        else:
            return Response({"Error": "No Author found"},status = 404)
# ----------------------------------------------------------------------------------------------------------

# Book related API's

class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        if books:
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        else:
            return Response({"Error": "No books found"},status = 404)

class BookCreateAPIView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookRetrieveAPIView(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class BookUpdateAPIView(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDeleteAPIView(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def delete(self, request, pk):
        book = self.get_object(pk)
        if book:
            book.delete()
            return Response({"Message":"Book deleted successfully"},status= 204)
        else:
            return Response({"Error": "No books found"},status = 404)
        
# ----------------------------------------------------------------------------------------

# Reading list related API's

class ReadingListCreateAPIView(APIView):
    def post(self, request):
        serializer = ReadingListSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReadingListRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return ReadingList.objects.get(pk=pk)
        except ReadingList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        reading_list = self.get_object(pk)
        serializer = ReadingListSerializer(reading_list)
        return Response(serializer.data)

    def put(self, request, pk):
        reading_list = self.get_object(pk)
        serializer = ReadingListSerializer(reading_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reading_list = self.get_object(pk)
        if reading_list:
            reading_list.delete()
            return Response({"Message":"Reading List deleted successfully"},status= 204)
        else:
            return Response({"Error": "No Reading List found"},status = 404)
