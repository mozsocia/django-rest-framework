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


class BookListCreateView(APIView):
    def get(self, request):
        books = Book.objects.all().prefetch_related('category')
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
