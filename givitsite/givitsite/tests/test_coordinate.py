from django.shortcuts import reverse
from django.test import Client, TestCase

URL_LIST = ['/coordinate/']
URL_NAME_LIST = ['coordinator_create_view']


class CoordinatePageTests_views_GET(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    # check the status code when navigate to the given url
    def test_request_status_code(self):
        for url in URL_LIST:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    # check url name
    def test_request_url_name(self):
        for url_name in URL_NAME_LIST:
            response = self.client.get(reverse(url_name))
            self.assertEqual(response.status_code, 200)

    # check if the correct template is being rendered
    def test_feed_correct_tamplate(self):
        response = self.client.get(reverse('coordinator_create_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'coordinator.html')


class CoordinatePageTests_views_POST(TestCase):
    def test_post_request_status_code(self):
        response = self.client.post(reverse('coordinator_create_view'))
        self.assertEqual(response.status_code, 302)
