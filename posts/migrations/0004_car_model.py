# Generated by Django 2.1.3 on 2018-11-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_car_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.CharField(choices=[(1, 'Ford'), (2, 'AUDI')], default=1, max_length=2),
        ),
    ]