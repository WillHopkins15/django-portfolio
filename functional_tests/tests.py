from selenium import webdriver
from django.test import Client
from django.contrib.auth.models import User
import unittest
import re

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

    def test_can_create_blog_post_and_edit(self):
        # Go to site with an admin session
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('William Hopkins', self.browser.title)

        # Click on add post button
        self.browser.find_element_by_class_name('glyphicon-plus').click()
        self.assertEqual(self.browser.current_url, 'http://127.0.0.1:8000/post/new/', "Was not redirected to new post page.")

        # Add a title and text to post
        self.browser.find_element_by_name('title').send_keys('Test Title')
        self.browser.find_element_by_name('text').send_keys('Test Text')

        # Click the save button
        self.browser.find_element_by_class_name('save').click()
        exp = re.compile('http://127.0.0.1:8000/post/\d+/')
        self.assertTrue(exp.match(self.browser.current_url) is not None, "Page not redirected when post saved.")
        post_no = self.browser.current_url.split('/')[4]

        # Return to the post list page and see our new post
        self.browser.get('http://127.0.0.1:8000')
        post_text = self.browser.find_element_by_xpath('//a[@href="'+'/post/'+str(post_no)+'/'+'"]')
        
        # Clicking on the post we just made brings it up on a new page.
        post_text.click()
        self.assertEqual(self.browser.current_url, 'http://127.0.0.1:8000/post/'+str(post_no)+'/')
        title = self.browser.find_element_by_tag_name('h2')
        text = self.browser.find_element_by_tag_name('p')
        self.assertEqual(title.text, 'Test Title')
        self.assertEqual(text.text, 'Test Text')

        # Click the edit button and modify the post and save again
        edit_btn = self.browser.find_element_by_class_name('glyphicon-pencil')
        edit_btn.click()
        self.browser.find_element_by_name('title').send_keys(' - Edit')
        self.browser.find_element_by_name('text').send_keys(' - Edit')
        self.browser.find_element_by_class_name('save').click()

        # Check whether post was updated
        self.browser.get('http://127.0.0.1:8000/post/'+str(post_no)+'/')
        title = self.browser.find_element_by_tag_name('h2')
        text = self.browser.find_element_by_tag_name('p')
        self.assertEqual(title.text, 'Test Title - Edit')
        self.assertEqual(text.text, 'Test Text - Edit')

    def test_cv(self):
        # Go to home page
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('William Hopkins', self.browser.title)

        # Click on cv button in header
        self.browser.find_element_by_class_name('cv').click()
        self.assertEqual(self.browser.current_url, 'http://127.0.0.1:8000/cv/')

        # I can view my cv on this page
        # Click the cv editor button
        # I edit my cv
        # I see that my cv has been updated

if __name__ == '__main__':
    unittest.main()