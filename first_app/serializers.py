from rest_framework import serializers
from .models import Person, Category, Book


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


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

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.create(**category_data)
        book = Book.objects.create(category=category, **validated_data)
        return book

    # def create(self, validated_data):
    #     category_id = validated_data.pop('category')
    #     category = Category.objects.get(id=category_id)
    #     book = Book.objects.create(category=category_id, **validated_data)
    #     return book
