from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from article.serializers import ArticleSerializer, CategorySerializer
from article.models import Article, Category
from rest_framework.permissions import AllowAny, IsAuthenticated
import django_filters


class ArticleViewSet(ModelViewSet):
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['category', 'id']
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class CategoryViewSet(ModelViewSet):
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id']
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
