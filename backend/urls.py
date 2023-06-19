from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from article.views import ArticleViewSet, CategoryViewSet


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('category', CategoryViewSet, basename='category')


def render_index(request):
    return render(request, "index.html")


def login_endpoint(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/login/', login_endpoint),
    re_path(r"^$", render_index),
    re_path(r"^(?:.*)/?$", render_index),
]
