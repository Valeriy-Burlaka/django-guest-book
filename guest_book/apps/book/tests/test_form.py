import os

from django.utils.unittest import TestCase

from ..forms import MessageForm


class TestMessageForm(TestCase):

    def setUp(self):
        os.environ['RECAPTCHA_TESTING'] = 'True'

    def tearDown(self):
        os.environ['RECAPTCHA_TESTING'] = 'False'

    def test_valid_form(self):
        # Set environment variable for django_recaptcha
        # 'PASSED' will be considered as valid value
        os.environ['RECAPTCHA_TESTING'] = 'True'
        # Form should be valid w/o 'homepage' field
        form_params = {'username': 'Valid User',
                       'email': 'test@example.com',
                       'message_body': 'Hello, guest book!',
                       'recaptcha_response_field': 'PASSED'}
        form = MessageForm(form_params)
        self.assertTrue(form.is_valid())
        form_data = form.cleaned_data
        self.assertEqual(form_data['username'], 'Valid User')
        self.assertEqual(form_data['email'], 'test@example.com')
        self.assertEqual(form_data['message_body'],
                         'Hello, guest book!')
