from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class ArticleSerializers(serializers.ModelSerializer):
    user_id = UserSerializers()

    class Meta:
        model = Article
        fields = '__all__'


class CreateArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class FavoriteArticleSerializers(serializers.ModelSerializer):
    article_id = ArticleSerializers()
    user_id = UserSerializers()

    class Meta:
        model = FavoriteArticle
        fields = '__all__'


class CreateFavoriteArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = FavoriteArticle
        fields = '__all__'


class CommentsSerializers(serializers.ModelSerializer):
    article_id = ArticleSerializers()
    user_id = UserSerializers()

    class Meta:
        model = Comments
        fields = '__all__'


class CreateCommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
