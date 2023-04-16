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
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all())

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['category'] = CategorySerializer(instance.category).data
        return ret

    class Meta:
        model = Book
        fields = '__all__'

```
views.py
```py
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

```

urls.py
```py
urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),

]