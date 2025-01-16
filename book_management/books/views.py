from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import MongoClient
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET'])
def average_price(request, year):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['book_management']
    collection = db['books_book']

    pipeline = [
        {"$match": {"published_date": {"$regex": f"^{year}"}}},
        {"$group": {"_id": None, "average_price": {"$avg": "$price"}}},
    ]
    result = list(collection.aggregate(pipeline))
    average_price = result[0]['average_price'] if result else 0

    return Response({"average_price": average_price})
