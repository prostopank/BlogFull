from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import *
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    favorite_articles = SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'password', 'favorite_articles']

    def get_favorite_articles(self, obj):
        filtered_favorite_articles = FavoriteArticle.objects.filter(user_id=obj.id)
        favorite_articles = CreateFavoriteArticleSerializers(filtered_favorite_articles, many=True).data
        return favorite_articles


class ArticleSerializers(serializers.ModelSerializer):
    user_id = UserSerializers()
    comments = SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    def get_comments(self, obj):
        filtered_comments = Comments.objects.filter(article_id=obj.id)
        comments = CommentsSerializers(filtered_comments, many=True).data
        return comments


class CreateArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class FavoriteArticleSerializers(serializers.ModelSerializer):
    article_id = ArticleSerializers()

    class Meta:
        model = FavoriteArticle
        fields = '__all__'


class CreateFavoriteArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = FavoriteArticle
        fields = '__all__'


class CommentsSerializers(serializers.ModelSerializer):
    user_id = UserSerializers()

    class Meta:
        model = Comments
        fields = '__all__'


class CreateCommentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
