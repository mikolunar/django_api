# Generated by Django 2.1.3 on 2018-12-03 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0019_auto_20181203_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='remote',
        ),
    ]
