# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table(u'book_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('user_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('message_text', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('user_homepage', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('user_addr', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, null=True, blank=True)),
            ('user_browser', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'book', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table(u'book_message')


    models = {
        u'book.message': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Message'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_text': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'user_addr': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'user_browser': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'user_homepage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['book']