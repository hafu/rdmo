# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-25 15:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0024_meta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attributeentity',
            options={'ordering': ('uri',), 'verbose_name': 'AttributeEntity', 'verbose_name_plural': 'AttributeEntities'},
        ),
        migrations.RenameField(
            model_name='attributeentity',
            old_name='description',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='attributeentity',
            old_name='title',
            new_name='key',
        ),
    ]
