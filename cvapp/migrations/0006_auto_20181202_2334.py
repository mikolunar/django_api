# Generated by Django 2.1.3 on 2018-12-02 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0005_auto_20181202_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Project Name'),
        ),
    ]
