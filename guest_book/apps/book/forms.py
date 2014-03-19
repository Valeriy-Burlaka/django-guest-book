import re

from django import forms
from captcha.fields import ReCaptchaField


class MessageForm(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs=\
                                        {'placeholder': 'Enter your name',
                                         'class': 'form-control input-sm'})
                               )
    email = forms.EmailField(max_length=100,
                             widget=forms.TextInput(attrs=\
                                        {'placeholder': 'Enter your email',
                                         'class': 'form-control input-sm'})
                             )
    homepage = forms.URLField(required=False, max_length=100,
                              widget=forms.TextInput(attrs=\
                                        {'placeholder': 'You may enter your site address',
                                         'class': 'form-control input-sm'})
                             )
    message_body = forms.CharField(max_length=750, min_length=1,
                                   widget=forms.Textarea(attrs=\
                                        {'id':'comment',
                                         'placeholder': 'Enter your message',
                                         'class': 'form-control input-sm',
                                         'rows': '4'})
                                  )
    captcha = ReCaptchaField(attrs={'theme': 'clean'})

    def clean_message_body(self):
        data = self.cleaned_data['message_body']
        # check if message totally consists of space characters
        # (spaces, line breaks)
        match = re.search(r'^\s+$', data)
        if match:
            raise forms.ValidationError("Please left us something more "
                                        "meaningful than blank message")
        return data

