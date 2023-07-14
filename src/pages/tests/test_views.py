from django.urls import reverse
from django.test import TestCase

from users.tests.factories import UserFactory


class HomePageViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('pages:home')
        cls.user = UserFactory()

    def test_home_page_view_for_anonymous_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Welcome to tunnels!')

    def test_home_page_view_for_logged_in__user(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, f'Hello, {self.user.username}')
