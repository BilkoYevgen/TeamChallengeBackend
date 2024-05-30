from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    SubCategoryListCreateView, SubCategoryDetailView,
    ProductListCreateView, ProductDetailView,
    ProductSubCategoryListCreateView, ProductSubCategoryDetailView
)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('subcategories/', SubCategoryListCreateView.as_view(), name='subcategory-list-create'),
    path('subcategories/<int:pk>/', SubCategoryDetailView.as_view(), name='subcategory-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product-subcategories/', ProductSubCategoryListCreateView.as_view(), name='productsubcategory-list-create'),
    path('product-subcategories/<int:pk>/', ProductSubCategoryDetailView.as_view(), name='productsubcategory-detail'),
]
