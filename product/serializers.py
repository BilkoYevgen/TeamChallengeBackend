from rest_framework import serializers
from product.models import Category, SubCategory, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']


class ProductSerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(
        source='subcategory_set', many=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image_urls', 'subcategories']
