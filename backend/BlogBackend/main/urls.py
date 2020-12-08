from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),
    path('auth/logout', Logout.as_view()),
    path('users', UsersListView.as_view()),

    path('article/all', ArticleListView.as_view()),
    path('article/detail/<int:pk>', ArticleDetailView.as_view()),
    path('article/create', CreateArticleView.as_view()),
    path('article/update/<int:pk>', UpdateArticleView.as_view()),
    path('article/delete/<int:pk>', DeleteArticleView.as_view()),

    path('comments/all', CommentsListView.as_view()),
    path('comments/create', CreateCommentView.as_view()),
    path('comments/update/<int:pk>', UpdateCommentView.as_view()),
    path('comments/delete/<int:pk>', DeleteCommentView.as_view()),

    path('favorite_articles/all', FavoriteArticleListView.as_view()),
    path('favorite_articles/create', CreateFavoriteArticleView.as_view()),
    path('favorite_articles/delete/<int:pk>', DeleteFavoriteArticleView.as_view())
]
