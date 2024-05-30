from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from product.models import Category, SubCategory, Product, ProductSubCategory
from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer, ProductSubCategorySerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListCreateView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductSubCategoryListCreateView(generics.ListCreateAPIView):
    queryset = ProductSubCategory.objects.all()
    serializer_class = ProductSubCategorySerializer


class ProductSubCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductSubCategory.objects.all()
    serializer_class = ProductSubCategorySerializer

