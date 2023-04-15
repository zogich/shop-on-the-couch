from django.shortcuts import render
from rest_framework import viewsets
from product.serializers import ProductSerializer, CategoriesSerializer
from product.models import Product, Category


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Category.objects.all()
