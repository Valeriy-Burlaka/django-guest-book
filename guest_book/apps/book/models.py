from django.utils import timezone
from django.db import models


class Message(models.Model):
    username = models.CharField(max_length=30)
    user_email = models.EmailField()
    message_text = models.TextField(max_length=500, )
    pub_date = models.DateTimeField()
    user_homepage = models.URLField(blank=True)
    user_addr = models.GenericIPAddressField(blank=True, null=True)
    user_browser = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-pub_date']

    def save(self, **kwargs):
        self.pub_date = timezone.now()
        super(Message, self).save(**kwargs)
