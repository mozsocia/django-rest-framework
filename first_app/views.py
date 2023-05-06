from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class CategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all().prefetch_related('product_set')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            product = Product.objects.filter(pk=pk).first()
            if not product:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ProductSerializerGet(product)
            return Response(serializer.data)
        else:
            products = Product.objects.all()
            serializer = ProductSerializerGet(products, many=True)
            return Response(serializer.data)


    # product json post 
    # { "name": "New Product", "price": 10.99,"categories": [1, 2, 3] }
    def post(self, request):
        serializer = ProductSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
