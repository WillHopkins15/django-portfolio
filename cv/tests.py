from django.test import TestCase
from django.urls import resolve
from cv.views import cv_view

# Create your tests here.
class CvBuilderPageTests(TestCase):

    def testCvUrlResolvesToView(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv_view)

    