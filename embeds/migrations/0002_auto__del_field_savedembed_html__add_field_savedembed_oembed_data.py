# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SavedEmbed.html'
        db.delete_column('embeds_savedembed', 'html')

        # Adding field 'SavedEmbed.oembed_data'
        db.add_column('embeds_savedembed', 'oembed_data',
                      self.gf('jsonfield.fields.JSONField')(default={}),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'SavedEmbed.html'
        db.add_column('embeds_savedembed', 'html',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'SavedEmbed.oembed_data'
        db.delete_column('embeds_savedembed', 'oembed_data')


    models = {
        'embeds.savedembed': {
            'Meta': {'unique_together': "(('url', 'maxwidth'),)", 'object_name': 'SavedEmbed'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'maxwidth': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'oembed_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['embeds']