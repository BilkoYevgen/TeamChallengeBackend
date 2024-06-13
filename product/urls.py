from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    SubCategoryListCreateView, SubCategoryDetailView,
    ProductListCreateView, ProductDetailView
)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('subcategories/', SubCategoryListCreateView.as_view(), name='subcategory-list-create'),
    path('subcategories/<int:pk>/', SubCategoryDetailView.as_view(), name='subcategory-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
