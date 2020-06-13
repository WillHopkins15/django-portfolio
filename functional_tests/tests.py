from selenium import webdriver
from django.test import Client
from django.contrib.auth.models import User
import unittest

class BasicSiteTest(unittest.TestCase):

    user = None

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.client = Client()
        self.user = User.objects.create_superuser(
            username='test',
            password='test',
            email='foo@bar.com',
        )
        self.client.force_login(self.user)
        cookie = self.client.cookies['sessionid']
        self.browser.get('http://127.0.0.1:8000/admin/')
        self.browser.add_cookie({'name': 'sessionid', 'value': cookie.value, 'secure': False, 'path': '/'})
        self.browser.refresh()

    def tearDown(self):
        self.user.delete()
        self.browser.quit()

    def test_can_create_blog_post(self):
        # Go to site with an admin session
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('William Hopkins', self.browser.title)

        # Click on add post button
        try:
            plus = self.browser.find_element_by_class_name('glyphicon-plus')
        except: 
            self.fail("Add post button not found. May not be admin")
        plus.click()
        self.assertEqual(self.browser.current_url, 'http://127.0.0.1:8000/post/new/', "Was not redirected to new post page.")

        # Add a title and text to post
        title = self.browser.find_element_by_name('title')
        text = self.browser.find_element_by_name('text')
        title.send_keys('Test title')
        text.send_keys('Test Text')

        # Click the save button
        save = self.browser.find_element_by_class_name('save')
        save.click()

        # View the post on a separate page
        

if __name__ == '__main__':
    unittest.main()