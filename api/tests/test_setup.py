from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post

class PostTests(APITestCase):
    def test_create_post(self):
        """
        Ensure we can create a new post object.
        """
        url = reverse('post-create')
        data = {'author': 'title'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().author, 'title')
