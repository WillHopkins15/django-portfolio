from django.test import TestCase
from django.urls import resolve
from django.contrib.auth.models import User
from blog.views import post_list

from .models import Post

# Create your tests here.
class HomePageTest(TestCase):

    testUser = None

    def setUp(self):
        self.testUser = User.objects.create_user(
            username='test',
            password='test',
            email='foo@bar.com',
        )
        self.post = Post()
        self.post.author = self.testUser
        self.post.title = 'A test post'
        self.post.text = 'Some sample text.'
        self.post.save()

    def tearDown(self):
        self.testUser.delete()

    def test_root_url_resolves_to_post_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

    def test_post_creation(self):
        retrieve = Post.objects.get(pk=self.post.id)
        self.assertEqual(retrieve, self.post)

    def test_post_publish(self):
        self.assertTrue(self.post.published_date is None)
        self.post.publish()
        self.assertTrue(self.post.published_date is not None)

    def test_post_to_string(self):
        self.assertEqual(self.post.__str__(), self.post.title)