from django.test import TestCase
from django.urls import reverse

from users.tests.factories import UserFactory


class UserViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.url_detail = reverse('users:detail', kwargs={'pk': cls.user.pk})
        cls.url_detail_fake = reverse('users:detail', kwargs={'pk': 0})

    def test_displaying_user_information(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/detail.html')
        self.assertContains(response, self.user.username)

    def test_not_displaying_user_information(self):
        response = self.client.get(self.url_detail_fake)
        self.assertEqual(response.status_code, 404)
