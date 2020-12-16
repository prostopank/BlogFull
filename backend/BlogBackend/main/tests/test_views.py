from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from main.models import Article
from main.models import Comments
from main.models import FavoriteArticle


class RegistrationUserTestCase(APITestCase):

    def test_registration(self):
        data = {
            "email": "DimaDima@gmail.com",
            "username": "DimaDima",
            "password": "Dima12345678"
        }

        response = self.client.post('/api/auth/users/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserLoginTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='Dima', password='some-very-strong-psw')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_user_authentication(self):
        response = self.client.get('/api/auth/users/me/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_un_authentication(self):
        self.client.force_authenticate(user=None)

        response = self.client.get('/api/auth/users/me/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ArticleViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='Dima', password='some-very-strong-psw')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        self.article = Article.objects.create(user_id=self.user, title='testTitle', body='testBody')

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_article_list_view(self):
        response = self.client.get('/api/article/all')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Article.objects.count(), 1)

    def test_article_detail_view(self):
        response = self.client.get('/api/article/detail/1')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 7)

    def test_article_create_view(self):
        data = {
            "title": "test_for_create",
            "body": "test_body_for_create",
            "views": 0,

        }

        response = self.client.post('/api/article/create', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_article_update_view(self):
        data = {
            "title": "test_for_update",
            "body": "test_body_for_update",
            "views": 0,

        }

        response = self.client.put('/api/article/update/1', data)
        article = Article.objects.get(id=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(article.title, 'test_for_update')

    def test_article_delete_view(self):
        Article.objects.create(user_id=self.user, title='testTitleForDelete', body='testBodyForDelete')

        response_delete = self.client.delete('/api/article/delete/2')
        response_get = self.client.get('/api/article/delete/2')

        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(Article.objects.count(), 1)


class CommentsViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='Dima', password='some-very-strong-psw')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        self.article = Article.objects.create(user_id=self.user, title='testTitle', body='testBody')
        self.comments = Comments.objects.create(user_id=self.user, article_id=self.article, body='testCommentsBody')

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_comments_list_view(self):
        response = self.client.get('/api/comments/all')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comments.objects.count(), 1)

    def test_comments_create_view(self):
        data = {
            "body": "test_body_for_create_comment",
            "article_id": 1,
            "user_id": 1
        }

        response = self.client.post('/api/comments/create', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_comments_update_view(self):
        data = {
            "body": "test_body_for_update_comment",
            "article_id": 1,
            "user_id": 1
        }

        response = self.client.put('/api/comments/update/1', data)
        comment = Comments.objects.get(id=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(comment.body, 'test_body_for_update_comment')

    def test_comments_delete_view(self):
        response_delete = self.client.delete('/api/comments/delete/1')
        response_get = self.client.get('/api/comments/delete/1')

        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(Comments.objects.count(), 0)


class FavoriteArticleViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Dima', password='some-very-strong-psw')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        self.article = Article.objects.create(user_id=self.user, title='testTitle', body='testBody')
        self.favorite_article = FavoriteArticle.objects.create(user_id=self.user, article_id=self.article)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_favorite_article_list_view(self):
        response = self.client.get('/api/favorite_articles/all')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(FavoriteArticle.objects.count(), 1)

    def test_favorite_article_create_view(self):
        data = {
            "article_id": 1,
            "user_id": 1
        }

        response = self.client.post('/api/favorite_articles/create', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FavoriteArticle.objects.count(), 2)

    def test_favorite_article_delete_view(self):
        response_delete = self.client.delete('/api/favorite_articles/delete/1')
        response_get = self.client.get('/api/favorite_articles/delete/1')

        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(FavoriteArticle.objects.count(), 0)
