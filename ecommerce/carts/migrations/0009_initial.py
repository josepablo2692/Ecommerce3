# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CartItem'
        db.create_table('carts_cartitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cart', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, to=orm['carts.Cart'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('line_total', self.gf('django.db.models.fields.DecimalField')(default=10.99, decimal_places=2, max_digits=1000)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True, null=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('carts', ['CartItem'])

        # Adding M2M table for field variations on 'CartItem'
        m2m_table_name = db.shorten_name('carts_cartitem_variations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cartitem', models.ForeignKey(orm['carts.cartitem'], null=False)),
            ('variation', models.ForeignKey(orm['products.variation'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cartitem_id', 'variation_id'])

        # Adding model 'Cart'
        db.create_table('carts_cart', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total', self.gf('django.db.models.fields.DecimalField')(default=0.0, decimal_places=2, max_digits=100)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('carts', ['Cart'])


    def backwards(self, orm):
        # Deleting model 'CartItem'
        db.delete_table('carts_cartitem')

        # Removing M2M table for field variations on 'CartItem'
        db.delete_table(db.shorten_name('carts_cartitem_variations'))

        # Deleting model 'Cart'
        db.delete_table('carts_cart')


    models = {
        'carts.cart': {
            'Meta': {'object_name': 'Cart'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'decimal_places': '2', 'max_digits': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'carts.cartitem': {
            'Meta': {'object_name': 'CartItem'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['carts.Cart']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line_total': ('django.db.models.fields.DecimalField', [], {'default': '10.99', 'decimal_places': '2', 'max_digits': '1000'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'variations': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'null': 'True', 'symmetrical': 'False', 'to': "orm['products.Variation']"})
        },
        'products.product': {
            'Meta': {'object_name': 'Product', 'unique_together': "(('title', 'slug'),)"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '29.99', 'decimal_places': '2', 'max_digits': '100'}),
            'sale_price': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '100', 'null': 'True', 'decimal_places': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'products.productimage': {
            'Meta': {'object_name': 'ProductImage'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'thumbnail': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'products.variation': {
            'Meta': {'object_name': 'Variation'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '120', 'default': "'size'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['products.ProductImage']"}),
            'price': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '100', 'null': 'True', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['products.Product']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['carts']