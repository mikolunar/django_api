# Generated by Django 2.1.3 on 2018-12-02 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0011_auto_20181203_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='current_location',
        ),
    ]
