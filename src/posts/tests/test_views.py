from django.test import TestCase
from django.urls import reverse

from posts.tests.factories import PostFactory
from users.tests.factories import UserFactory


class PostViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.url = reverse('posts:list')

    def test_displaying_list_of_posts(self):
        post = PostFactory(author=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/list.html')
        self.assertContains(response, post.text)

    def test_not_displaying_list_of_posts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/list.html')
        self.assertContains(response, 'There are no posts.')
