from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.


class HomePageTest(SimpleTestCase):
    """test  the home page"""
    def setUp(self):
        """set up the client response"""
        url = reverse('home')
        self.response = self.client.get(url)
    
    def test_url_exist_at_correct_location(self):
        """test whether the url exist at the correct location"""
        self.assertEqual(self.response.status_code, 200)
        
    def test_homepage_url_name(self):
        """test whether home page exist with name home"""
        self.assertEqual(self.response.status_code, 200)
        
    def test_homepage_template(self):
        """test the template used for the home page"""
        self.assertTemplateUsed(self.response, 'home.html')
        
    def test_homepage_contains_correct_html(self):
        """check whether html file content is correct"""
        self.assertContains(self.response, "home page")

    def test_homepage_does_not_contain_incorrect_html(self):
        """check whether home page contains correct html content"""
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")
