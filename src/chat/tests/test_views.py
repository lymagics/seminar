from django.test import TestCase
from django.urls import reverse

from chat.tests.factories import ChatFactory, MessageFactory
from users.tests.factories import UserFactory


class ChatViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.other = UserFactory()
        cls.chat = ChatFactory(initiator=cls.user, participant=cls.other)
        cls.url = reverse('chat:room', kwargs={'pk': cls.other.pk})

    def test_retrieving_empty_chat(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat.html')
        self.assertContains(response, 'You will be the first one.')

    def test_retrieving_chat_with_messages(self):
        messages = MessageFactory.create_batch(5, author=self.user, chat=self.chat)
        self.client.force_login(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat.html')
        for message in messages:
            self.assertContains(response, message.text)

    def test_retrieving_chat_with_yourself(self):
        self.client.force_login(user=self.user)
        url = reverse('chat:room', kwargs={'pk': self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
