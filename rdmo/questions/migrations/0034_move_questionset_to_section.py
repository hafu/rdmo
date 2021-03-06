# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-29 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0033_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionset',
            name='section',
            field=models.ForeignKey(help_text='The section this questionset belongs to.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questionsets', to='questions.Section', verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='questionset',
            name='title_de',
            field=models.CharField(help_text='The German title for this subsection.', max_length=256, null=True, verbose_name='Title (de)'),
        ),
        migrations.AddField(
            model_name='questionset',
            name='title_en',
            field=models.CharField(help_text='The English title for this subsection.', max_length=256, null=True, verbose_name='Title (en)'),
        ),
    ]
