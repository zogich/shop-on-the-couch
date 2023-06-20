from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from article.serializers import ArticleSerializer, CategorySerializer
from article.models import Article, Category
from rest_framework.permissions import AllowAny, IsAuthenticated


class ArticleViewSet(ModelViewSet):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
