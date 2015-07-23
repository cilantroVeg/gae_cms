"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        from pages.models import *
        from users.models import *
        language = Language.objects.create(name="English",code="en")
        category = Category.objects.create(name="Category 1",language=language)
        user = User.objects.create_user(username='test',email='test@test.com',password='password')
        page = Page.objects.create(title="Page 1",content="Page 1",category=category,user=user)
        self.assertEqual(1 + 1, 2)

