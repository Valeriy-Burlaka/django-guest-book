import os

from django.utils.unittest import TestCase

from ..forms import MessageForm


class TestMessageForm(TestCase):

    def setUp(self):
        os.environ['RECAPTCHA_TESTING'] = 'True'

    def tearDown(self):
        os.environ['RECAPTCHA_TESTING'] = 'False'

    def test_clean_valid_form_wo_captcha(self):
        form_params = {'recaptcha_response_field': 'PASSED'}
        form = MessageForm(form_params)
        self.assertTrue(form.is_valid())