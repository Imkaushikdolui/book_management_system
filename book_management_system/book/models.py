from django.db import models
from apiauth.models import Account

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    book_file = models.FileField(upload_to='books/', blank=True, null=True)

    def __str__(self):
        return self.title

class ReadingList(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, related_name='reading_lists')

    def __str__(self):
        return self.name
