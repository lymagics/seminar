from django.test import TestCase
from django.urls import reverse

from posts.tests.factories import PostFactory, LikeFactory
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

    def test_like_post(self):
        post = PostFactory(author=self.user)
        url = reverse('posts:like', kwargs={'pk': post.pk})
        self.client.force_login(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        post.refresh_from_db()
        self.assertIn(self.user, post.get_liked_users())

    def test_unlike_post(self):
        post = PostFactory(author=self.user)
        LikeFactory(post=post, user=self.user)
        url = reverse('posts:unlike', kwargs={'pk': post.pk})
        self.client.force_login(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        post.refresh_from_db()
        self.assertNotIn(self.user, post.get_liked_users())

    def test_display_post_likes(self):
        post = PostFactory(author=self.user)
        LikeFactory(post=post, user=self.user)
        self.client.force_login(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/list.html')
        self.assertContains(response, '1 like(s)')
