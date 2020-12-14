import json

from django.contrib.auth.models import User
from django.test import SimpleTestCase
from django.urls import reverse, resolve, include, path
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APISimpleTestCase, URLPatternsTestCase

from main import models
from main import serializers
from main import views


class TestUrls(APITestCase):

    def test_users_url_is_resolves(self):
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_article_all_is_resolves(self):
        response = self.client.get('/api/article/all')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_article_detail_is_resolves(self):
        response = self.client.get('/api/article/detail/1')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
