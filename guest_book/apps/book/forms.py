from django import forms
from captcha.fields import ReCaptchaField


class MessageForm(forms.Form):
    captcha = ReCaptchaField()

