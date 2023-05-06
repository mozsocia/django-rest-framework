from rest_framework import serializers
from .models import Person, Category, Book


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class BookSerializerPost(serializers.ModelSerializer):

    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all())

    class Meta:
        model = Book
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    book_set = BookSerializerPost(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'



class BookSerializerGet(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'



