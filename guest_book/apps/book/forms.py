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
    message_body = forms.CharField(max_length=500, min_length=1,
                                   widget=forms.Textarea(attrs=\
                                        {'placeholder': 'Enter your message',
                                         'class': 'form-control input-sm',
                                         'rows': '4'})
                                  )
    captcha = ReCaptchaField(attrs={'theme': 'clean'})

