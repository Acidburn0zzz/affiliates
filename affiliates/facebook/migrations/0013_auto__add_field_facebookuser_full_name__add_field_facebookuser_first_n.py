# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FacebookUser.full_name'
        db.add_column('facebook_facebookuser', 'full_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=256, blank=True),
                      keep_default=False)

        # Adding field 'FacebookUser.first_name'
        db.add_column('facebook_facebookuser', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=256, blank=True),
                      keep_default=False)

        # Adding field 'FacebookUser.last_name'
        db.add_column('facebook_facebookuser', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=256, blank=True),
                      keep_default=False)

        # Adding field 'FacebookUser.locale'
        db.add_column('facebook_facebookuser', 'locale',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FacebookUser.full_name'
        db.delete_column('facebook_facebookuser', 'full_name')

        # Deleting field 'FacebookUser.first_name'
        db.delete_column('facebook_facebookuser', 'first_name')

        # Deleting field 'FacebookUser.last_name'
        db.delete_column('facebook_facebookuser', 'last_name')

        # Deleting field 'FacebookUser.locale'
        db.delete_column('facebook_facebookuser', 'locale')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'facebook.facebookaccountlink': {
            'Meta': {'object_name': 'FacebookAccountLink'},
            'activation_code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'affiliates_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'account_links'", 'to': "orm['auth.User']"}),
            'facebook_user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'_account_link'", 'unique': 'True', 'to': "orm['facebook.FacebookUser']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'facebook.facebookbanner': {
            'Meta': {'object_name': 'FacebookBanner'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '250'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Banner'", 'unique': 'True', 'max_length': '255'})
        },
        'facebook.facebookbannerinstance': {
            'Meta': {'object_name': 'FacebookBannerInstance'},
            'banner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['facebook.FacebookBanner']"}),
            'can_be_an_ad': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'custom_image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'total_clicks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'banner_instance_set'", 'to': "orm['facebook.FacebookUser']"})
        },
        'facebook.facebookbannerlocale': {
            'Meta': {'object_name': 'FacebookBannerLocale'},
            'banner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locale_set'", 'to': "orm['facebook.FacebookBanner']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locale': ('affiliates.base.models.LocaleField', [], {'default': "'en-US'", 'max_length': '32'})
        },
        'facebook.facebookclickstats': {
            'Meta': {'object_name': 'FacebookClickStats'},
            'banner_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['facebook.FacebookBannerInstance']"}),
            'clicks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hour': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 8, 23, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'facebook.facebookuser': {
            'Meta': {'object_name': 'FacebookUser'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'leaderboard_position': ('django.db.models.fields.IntegerField', [], {'default': '2147483647'}),
            'locale': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'total_clicks': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['facebook']
