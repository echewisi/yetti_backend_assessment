# tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model  # Import get_user_model
from .forms import CustomLoginForm, RegistrationForm  # Import your forms
from django.contrib import messages

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'password1': 'password123',
            'password2': 'password123',
        }
        self.user = User.objects.create_user(username='test@example.com', password='password123')

    def test_registration_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')
        self.assertContains(response, 'csrfmiddlewaretoken')

        response = self.client.post(reverse('register'), data=self.user_data)
        self.assertEqual(response.status_code, 200)  # Redirect on successful registration
        self.assertTrue(User.objects.filter(username='test@example.com').exists())

    def test_custom_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')
        self.assertContains(response, 'csrfmiddlewaretoken')
            # Log in the user
        logged_in = self.client.login(username='test@example.com', password='password123')
        self.assertTrue(logged_in)  # Check if the user is logged in

        # Check the session
        user_id = self.client.session.get('_auth_user_id')
        self.assertIsNotNone(user_id)  # Ensure that the user_id is in the session

        response = self.client.post(reverse('login'), data=self.user_data)
        self.assertEqual(response.status_code, 200)  # Redirect on successful login
        self.assertTrue(self.client.session['_auth_user_id'])  # Check if the user is logged in

    def test_authentication_required_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)  # Redirect to login page for unauthenticated users

    def test_incorrect_login(self):
        response = self.client.post(reverse('login'), data={'email': 'test@example.com', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, 200)  # Login failed, should stay on login page

    def test_nonexistent_user_login(self):
        response = self.client.post(reverse('login'), data={'email': 'nonexistent@example.com', 'password': 'password123'})
        self.assertEqual(response.status_code, 200)  # Non-existent user, should stay on login page

    def test_security_vulnerabilities(self):
        # Test for potential security vulnerabilities (e.g., session fixation and CSRF attacks)

        # Example CSRF test (ensure CSRF protection is enabled)
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'csrfmiddlewaretoken')

        # Session Fixation Test
        # Create a session with a known session ID
        session = self.client.session
        session['_session_id'] = 'known_session_id'
        session.save()

        # Attempt to log in with the known session ID
        response = self.client.post(reverse('login'), data={'email': 'test@example.com', 'password': 'password123'})
        self.assertEqual(response.status_code, 200)  # Session fixation attempt should fail

        # Cleanup: Clear the session to prevent conflicts with other tests
        self.client.session.flush()
