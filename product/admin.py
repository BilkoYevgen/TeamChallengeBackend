from django.contrib import admin
from .models import Category, SubCategory, Product, ProductSubCategory

admin.site.register([Category, SubCategory, Product, ProductSubCategory])
    
    
