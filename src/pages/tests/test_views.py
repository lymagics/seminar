from django.urls import reverse
from django.test import TestCase

import faker

from users.tests.factories import UserFactory


class HomePageViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('pages:home')
        cls.user = UserFactory()
        cls.faker = faker.Faker()

    def test_home_page_view_for_anonymous_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_home_page_view_for_logged_in_user(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'What is on your mind?')

    def test_creating_new_post(self):
        self.client.force_login(user=self.user)
        new_post = {
            'text': self.faker.paragraph(),
        }
        response = self.client.post(self.url, new_post)
        self.assertEqual(response.status_code, 302)

        self.user.refresh_from_db()
        post = self.user.posts.first()
        self.assertIsNotNone(post)
        self.assertEqual(post.text, new_post['text'])
