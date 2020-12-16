from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework.views import APIView

from .models import *
from .serializers import *
from .permissions import IsOwnerOrReadOnly


# USER
class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


# ARTICLE
class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers


class ArticleDetailView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers


class CreateArticleView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = CreateArticleSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class UpdateArticleView(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = CreateArticleSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user)


class DeleteArticleView(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = CreateArticleSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# COMMENTS
class CommentsListView(generics.ListAPIView):
    serializer_class = CommentsSerializers
    queryset = Comments.objects.all()


class CreateCommentView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CreateCommentsSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class UpdateCommentView(generics.RetrieveUpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CreateCommentsSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user)


class DeleteCommentView(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = CreateArticleSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# FAVORITE ARTICLES
class FavoriteArticleListView(generics.ListAPIView):
    serializer_class = FavoriteArticleSerializers
    queryset = FavoriteArticle.objects.all()


class CreateFavoriteArticleView(generics.CreateAPIView):
    queryset = FavoriteArticle.objects.all()
    serializer_class = CreateFavoriteArticleSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class DeleteFavoriteArticleView(generics.RetrieveDestroyAPIView):
    queryset = FavoriteArticle.objects.all()
    serializer_class = CreateFavoriteArticleSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
