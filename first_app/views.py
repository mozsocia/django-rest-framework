from .serializers import CategorySerializer
from .models import Category
from .serializers import BookSerializer
from .models import Book
from .serializers import PersonSerializer
from .models import Person
from rest_framework import generics
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Person
from .serializers import PersonSerializer
from rest_framework import status


@api_view(['GET'])
def home(request):
    return Response({'message': 'Hello, World!'})


class PersonListCreateView(generics.GenericAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request):
        persons = self.get_queryset()
        serializer = self.get_serializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py
# class BookListCreateView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class CategoryListAPIView(APIView):

    def get(self, request, format=None):
        # categories = Category.objects.all().prefetch_related('book_set')
        # serializer = CategorySerializer(categories, many=True)
        # return Response(serializer.data)

        categories = Category.objects.all()
        category_data = []
        for category in categories:
            category_books = Book.objects.filter(category=category)
            category_serializer_data = CategorySerializer(category).data

            category_serializer_data['books'] = BookSerializer(
                category_books, many=True).data
            category_data.append(category_serializer_data)
        return Response(category_data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookListCreateView(APIView):
    def get(self, request):
        # books = Book.objects.all()
        # serializer = BookSerializer(books, many=True)
        # return Response(serializer.data)

        books = Book.objects.all()
        book_data = []
        for book in books:
            book_serializer_data = BookSerializer(book).data
            book_serializer_data['category'] = CategorySerializer(
                book.category).data

            book_data.append(book_serializer_data)
        return Response(book_data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
