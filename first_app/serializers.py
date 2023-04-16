from rest_framework import serializers
from .models import Person, Category, Book


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


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
