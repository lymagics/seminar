from django.urls import reverse
from django.test import SimpleTestCase


class HomePageViewTest(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = reverse('pages:home')

    def test_home_page_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Home page')
