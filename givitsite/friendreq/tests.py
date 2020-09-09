from django.test import TestCase 
from django.shortcuts import reverse
from django.contrib.auth.models import User
from .models import ItemRequest,ItemsFound
from django.conf import settings

class FriendPageTests(TestCase):
    # check the status code when navigate to request page
    def test_request_status_code(self):
        response = self.client.get('/friend/request')
        self.assertEquals(response.status_code,200)

    # check url name
    def test_request_url_name(self):
        response = self.client.get(reverse('itemRequest_create_view'))
        self.assertEquals(response.status_code,200)

    # check the status code when navigate to feed page
    def test_feed_status_code(self):
        response = self.client.get('/friend/feed')
        self.assertEquals(response.status_code,200)

    # check url name
    def test_feed_url_name(self):
        response = self.client.get(reverse('requestItem'))
        self.assertEquals(response.status_code,200)

    # check if the correct template is being rendered
    def test_feed_correct_tamplate(self):
        response = self.client.get(reverse('requestItem'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'feed.html')

class ItemRequest_test(TestCase):
    @classmethod
    def setUp(cls):
        test_user = User.objects.filter(is_superuser=True)
        ItemRequest.objects.create(special_req = "this is a Test", friend_id =test_user[0])
    
    def test_text(self):
        #check insersion of request to the ItemRequest table
        test_user = User.objects.filter(is_superuser=True)
        req =  ItemRequest.objects.get(friend_id =test_user[0])
        expected_special_request = req.special_req
        self.assertEquals(expected_special_request,"this is a Test")

 