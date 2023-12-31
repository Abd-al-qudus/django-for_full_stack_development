from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.


class CustomUserTest(TestCase):
    """test the custom user class"""
    def test_create_user(self):
        """test create user"""
        User = get_user_model()
        user = User.objects.create_user(username="will", password="test1234", email="will@gmail.com")
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_superuser(self):
        """create a superuser"""
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin", email="admin@gmail.com", password="testpass123"
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'admin@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        