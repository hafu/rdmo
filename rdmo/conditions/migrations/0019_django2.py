# Generated by Django 2.2rc1 on 2019-03-26 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0018_remove_null_true'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='condition',
            options={'ordering': ('uri',), 'verbose_name': 'Condition', 'verbose_name_plural': 'Conditions'},
        ),
    ]
