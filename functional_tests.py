from selenium import webdriver
import unittest

class BasicSiteTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def testBrowserTitle(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Django Girls blog', self.browser.title)

if __name__ == '__main__':
    unittest.main()