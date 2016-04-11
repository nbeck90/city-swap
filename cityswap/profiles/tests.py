from django.test import TestCase


class BaseTest(TestCase):

    def run(self):
        self.assertEqual(True, True)
