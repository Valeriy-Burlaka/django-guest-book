from django import forms
from captcha.fields import ReCaptchaField


class MessageForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    homepage = forms.URLField(required=False)
    message_body = forms.CharField(max_length=500, min_length=1)
    captcha = ReCaptchaField()

