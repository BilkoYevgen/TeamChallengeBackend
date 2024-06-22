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
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image_urls', 'subcategories']

    def create(self, validated_data):
        subcategories_data = validated_data.pop('subcategories')

        if Product.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError("Product with this name already exists.")

        product = Product.objects.create(**validated_data)

        for subcategory_data in subcategories_data:
            category_id = subcategory_data['category'].id
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                raise serializers.ValidationError(f"Category with id {category_id} does not exist.")

            try:
                subcategory = SubCategory.objects.get(
                    name=subcategory_data['name'],
                    category=category
                )
            except SubCategory.DoesNotExist:
                raise serializers.ValidationError(
                    f"Subcategory with name '{subcategory_data['name']}' and category id '{category_id}' does not exist."
                )

            product.subcategories.add(subcategory)

        return product


