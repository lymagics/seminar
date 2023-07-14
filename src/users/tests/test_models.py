from django.test import TestCase

from users.tests.factories import UserFactory


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.follower = UserFactory()

    def test_follow_user(self):
        self.follower.follow(self.user)
        self.assertTrue(self.follower.is_following(self.user))

    def test_unfollow_user(self):
        self.follower.following.add(self.user)
        self.assertTrue(self.follower.is_following(self.user))
        self.follower.unfollow(self.user)
        self.assertFalse(self.follower.is_following(self.user))

    def test_check_is_following(self):
        self.assertEqual(self.follower.is_following(self.user), False)
        self.follower.following.add(self.user)
        self.assertEqual(self.follower.is_following(self.user), True)
