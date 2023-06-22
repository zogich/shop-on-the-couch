from article.models import Category, Article

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ArticleSerializer, self).to_representation(instance)
        representation['category'] = instance.category.name
        return representation
