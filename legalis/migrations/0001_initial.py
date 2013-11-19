# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Operation'
        db.create_table('operations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'legalis', ['Operation'])


    def backwards(self, orm):
        # Deleting model 'Operation'
        db.delete_table('operations')


    models = {
        u'legalis.operation': {
            'Meta': {'object_name': 'Operation', 'db_table': "'operations'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '90'})
        }
    }

    complete_apps = ['legalis']