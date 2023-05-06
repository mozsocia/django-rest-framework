from rest_framework import serializers
from .models import *



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class CategorySerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many=True , read_only=True)
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializerGet(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'categories']

class ProductSerializerPost(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'categories']

    # def create(self, validated_data):
    #     print(validated_data)
    #     categories_data = validated_data.pop('categories')
    #     product = Product.objects.create(**validated_data)
    #     for category_id in categories_data:
    #         category = Category.objects.get(id=category_id)
    #         product.categories.add(category)
    #     return product

    # def update(self, instance, validated_data):
    #     categories_data = validated_data.pop('categories')
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.categories.clear()
    #     for category_id in categories_data:
    #         category = Category.objects.get(id=category_id)
    #         instance.categories.add(category)
    #     instance.save()
        # return instance
