from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet, CategoryViewSet
from django.shortcuts import render

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('category', CategoryViewSet, basename='category')


def render_react(request):
    return render(request, "index.html")


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    re_path(r"^$", render_react),
    re_path(r"^(?:.*)/?$", render_react),
]
