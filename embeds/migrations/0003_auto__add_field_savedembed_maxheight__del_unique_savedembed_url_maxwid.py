# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'SavedEmbed', fields ['url', 'maxwidth']
        db.delete_unique('embeds_savedembed', ['url', 'maxwidth'])

        # Adding field 'SavedEmbed.maxheight'
        db.add_column('embeds_savedembed', 'maxheight',
                      self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'SavedEmbed', fields ['url', 'maxheight', 'maxwidth']
        db.create_unique('embeds_savedembed', ['url', 'maxheight', 'maxwidth'])


    def backwards(self, orm):
        # Removing unique constraint on 'SavedEmbed', fields ['url', 'maxheight', 'maxwidth']
        db.delete_unique('embeds_savedembed', ['url', 'maxheight', 'maxwidth'])

        # Deleting field 'SavedEmbed.maxheight'
        db.delete_column('embeds_savedembed', 'maxheight')

        # Adding unique constraint on 'SavedEmbed', fields ['url', 'maxwidth']
        db.create_unique('embeds_savedembed', ['url', 'maxwidth'])


    models = {
        'embeds.savedembed': {
            'Meta': {'unique_together': "(('url', 'maxwidth', 'maxheight'),)", 'object_name': 'SavedEmbed'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'maxheight': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maxwidth': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'oembed_data': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['embeds']