# Generated by Django 2.1.3 on 2018-11-20 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='model',
        ),
    ]
