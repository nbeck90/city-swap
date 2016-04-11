from django.test import TestCase
from requests.models import Request
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfileTest(TestCase):
    def setUp(self):
        User.objects.create_user('frank', password='bar')
        f = Profile.objects.get()
        Request.objects.create(title='test', description='things', sender=f)

    def test_description_title(self):
        f = Profile.objects.get()
        test_request = Request.objects.get(sender=f)
        self.assertEqual(test_request.description, 'things')
        self.assertEqual(test_request.title, 'test')
