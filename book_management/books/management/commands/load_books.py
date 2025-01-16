from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = "Load initial book data"

    def handle(self, *args, **kwargs):
        books = [
            {"title": "Book 1", "author": "Author 1", "published_date": "2020-01-01", "genre": "Fiction", "price": 29.99},
            {"title": "Book 2", "author": "Author 2", "published_date": "2021-05-15", "genre": "Non-fiction", "price": 19.99},
            # Agrega más libros aquí...
        ]
        for book in books:
            Book.objects.create(**book)
        self.stdout.write("Books loaded successfully!")
