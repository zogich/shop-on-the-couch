from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from article.views import ArticleViewSet, CategoryViewSet
from django.http import HttpResponse


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('category', CategoryViewSet, basename='category')


def render_index(request):
    return render(request, "index.html")


urlpatterns = [
    path('api/', include(router.urls)),
    path(r'api/auth/', include('djoser.urls')),
    path(r'api/auth/', include('djoser.urls.authtoken')),
    path(r'api/auth/', include('djoser.urls.jwt')),
    path('admin/', admin.site.urls),
    re_path(r"^$", render_index),
    re_path(r"^(?:.*)/?$", render_index),
]
