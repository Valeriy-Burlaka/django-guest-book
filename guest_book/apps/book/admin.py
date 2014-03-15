from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    fields = ['username', 'user_email', 'message_text']

admin.site.register(Message, MessageAdmin)