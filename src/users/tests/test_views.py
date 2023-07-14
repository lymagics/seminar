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
        cls.url_follow = reverse('users:follow', kwargs={'pk': cls.user.pk})
        cls.url_unfollow = reverse('users:unfollow', kwargs={'pk': cls.user.pk})
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

    def test_follow_user(self):
        follower = UserFactory()
        self.client.force_login(user=follower)
        response = self.client.get(self.url_follow)
        self.assertEqual(response.status_code, 302)
        follower.refresh_from_db()
        self.assertTrue(follower.is_following(self.user))

    def test_unfollow_user(self):
        follower = UserFactory()
        follower.follow(self.user)
        self.client.force_login(user=follower)
        response = self.client.get(self.url_unfollow)
        self.assertEqual(response.status_code, 302)
        follower.refresh_from_db()
        self.assertFalse(follower.is_following(self.user))

    def test_follow_counter_change(self):
        follower = UserFactory()
        follower.follow(self.user)
        self.user.follow(follower)
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/detail.html')
        self.assertContains(response, 'Followers: 1')
        self.assertContains(response, 'Following: 1')
