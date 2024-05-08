from django.urls import path
from .views import (
    BookListAPIView,
    BookCreateAPIView,
    BookRetrieveAPIView,
    BookUpdateAPIView,
    BookDeleteAPIView,
    AuthorCreateAPIView,
    AuthorUpdateAPIView,
    AuthorDeleteAPIView,
    ReadingListCreateAPIView,
    ReadingListRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Author related urls
    
    # Create a new Author
    path('author/create/', AuthorCreateAPIView.as_view(), name='Author-create'),

    # Update a specific Author
    path('author/update/<int:pk>/', AuthorUpdateAPIView.as_view(), name='Author-update'),

    # Delete a specific Author
    path('author/delete/<int:pk>/', AuthorDeleteAPIView.as_view(), name='Author-delete'),
    # -----------------------------------------------------------------------------------------
    
    # Books related urls
    
    # List all books
    path('booklist/', BookListAPIView.as_view(), name='book-list'),

    # Retrieve a specific book
    path('booklist/<int:pk>/', BookRetrieveAPIView.as_view(), name='book-retrieve'),

    # Create a new book
    path('create/', BookCreateAPIView.as_view(), name='book-create'),

    # Update a specific book
    path('update/<int:pk>/', BookUpdateAPIView.as_view(), name='book-update'),

    # Delete a specific book
    path('delete/<int:pk>/', BookDeleteAPIView.as_view(), name='book-delete'),
    # -----------------------------------------------------------------------------------------
    
    # Reading list related urls
    
    # Create a new reading list
    path('reading-lists/', ReadingListCreateAPIView.as_view(), name='reading-list-create'),

    # Retrieve, update, or delete a specific reading list
    path('reading-lists/<int:pk>/', ReadingListRetrieveUpdateDestroyAPIView.as_view(), name='reading-list-detail'),
    
]
