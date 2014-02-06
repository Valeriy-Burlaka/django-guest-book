from django.utils.unittest import TestCase

from ..models import Message


class TestMessage(TestCase):

    def test_message_save(self):
        message = Message(username='Test',
                          user_email='test@test.com',
                          message_text='hello guest book',
                          user_homepage='http://example.com',
                          user_addr='192.168.0.1',
                          user_browser='Chrome')
        message.save()
        self.assertEqual(len(Message.objects.all()), 1)