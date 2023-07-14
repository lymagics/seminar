from django.test import TestCase
from django.urls import reverse

import faker

from users.tests.factories import UserFactory


class UserViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.url_detail = reverse('users:detail', kwargs={'pk': cls.user.pk})
        cls.url_detail_fake = reverse('users:detail', kwargs={'pk': 0})
        cls.url_edit = reverse('users:edit')
        cls.faker = faker.Faker()

    def test_displaying_user_information(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/detail.html')
        self.assertContains(response, self.user.username)

    def test_not_displaying_user_information(self):
        response = self.client.get(self.url_detail_fake)
        self.assertEqual(response.status_code, 404)

    def test_editing_user_information_page(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.url_edit)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/edit.html')
        self.assertContains(response, self.user.username)

    def test_editing_user_information(self):
        self.client.force_login(user=self.user)
        new_data = {
            'username': self.faker.user_name(),
            'about_me': self.faker.paragraph(),
        }
        response = self.client.post(self.url_edit, new_data)
        self.assertEqual(response.status_code, 302)

        self.user.refresh_from_db()
        self.assertEqual(self.user.username, new_data['username'])
        self.assertEqual(self.user.about_me, new_data['about_me'])

    def test_editing_user_information_fail_for_anonymous_user(self):
        response = self.client.get(self.url_edit)
        self.assertEqual(response.status_code, 302)
