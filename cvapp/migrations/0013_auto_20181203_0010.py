# Generated by Django 2.1.3 on 2018-12-02 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0012_remove_cv_current_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='Location',
            new_name='location',
        ),
    ]
