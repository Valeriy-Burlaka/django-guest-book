from django.utils.unittest import TestCase

from ..models import Message


class TestMessage(TestCase):

    def setUp(self):
        self.message_data = {'username': 'Test',
                             'user_email': 'test@test.com',
                             'message_text': 'hello guest book',
                             'user_homepage': 'http://example.com',
                             'user_addr': '192.168.0.1',
                             'user_browser': 'Chrome'}

    def test_message_save(self):
        message = Message(**self.message_data)
        message.save()
        self.assertEqual(len(Message.objects.all()), 1)

    def test_convert_message_text(self):
        """
        Tests that input text was sanitized & postmarkup'ed
        (Allowed postmarkup BBCodes: ['b', 'i', 'url', 's', 'u'])
        """
        message = Message(**self.message_data)
        # HTML tags sanitized, BBCodes converted back to tags
        # and automatically closed
        input_text = "<b>Peter went to<script>alert(2)</script>" \
                     "[b]one[i]word[s]for[u]each[url=http://www.example.com]issue[/url]"
        saved_text = u"&lt;b&gt;Peter went to&lt;script&gt;alert(2)&lt;/script&gt;" \
                     "<strong>one<em>word<strike>for<u>each" \
                     "<a href=\"http://www.example.com\">issue</a></u></strike></em></strong>"
        self.assertEqual(message.convert_message_text(input_text), saved_text)
