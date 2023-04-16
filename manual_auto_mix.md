models.py
```py
# models.py
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    book_title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_title
```


serializers.py
```py

class BookSerializer(serializers.ModelSerializer):

    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all())

    class Meta:
        model = Book
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    book_set = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

```
views.py
```py


class CategoryListAPIView(APIView):

    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookListCreateView(APIView):
    def get(self, request):

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

```

urls.py
```py
urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),

]