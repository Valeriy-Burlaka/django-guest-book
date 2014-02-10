from django.utils import timezone
from django.db import models
import postmarkup


class Message(models.Model):
    username = models.CharField(max_length=30)
    user_email = models.EmailField()
    message_text = models.TextField(max_length=500)
    pub_date = models.DateTimeField()
    user_homepage = models.URLField(blank=True)
    user_addr = models.GenericIPAddressField(blank=True, null=True)
    user_browser = models.CharField(max_length=100, blank=True)

    ALLOWED_MARKUP = ['b', 's', 'u', 'i']  # Allowed BBCodes

    class Meta:
        verbose_name_plural = 'Messages'
        ordering = ['-pub_date']

    def save(self, **kwargs):
        self.pub_date = timezone.now()
        self.message_text = self.convert_message_text(self.message_text)
        super(Message, self).save(**kwargs)

    def __unicode__(self):
        return "{name} | {email} | {date}".format(name=self.username,
                                                  email=self.user_email,
                                                  date=self.pub_date)

    def convert_message_text(self, message_text):
        class MyLinkTag(postmarkup.LinkTag):
            """
            Overrides annotate_link behavior in LinkTag
            """
            def __init__(self, name, **kwargs):
                postmarkup.LinkTag.__init__(self, name,
                                            annotate_links=False, **kwargs)

        markup = postmarkup.create(include=self.ALLOWED_MARKUP,
                                   use_pygments=False)
        markup.add_tag(MyLinkTag, u'url')
        return markup(message_text)


