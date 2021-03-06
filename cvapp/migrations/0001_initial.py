# Generated by Django 2.1.3 on 2018-12-01 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('mobile', models.CharField(blank=True, max_length=12)),
                ('facebook', models.URLField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('remark', models.CharField(blank=True, max_length=20)),
                ('cv_types', models.CharField(choices=[('SARCH', 'Solution Architect'), ('DEV', 'Developer'), ('SENG', 'Software Engineer')], default='SENG', max_length=5)),
                ('cv_lang', models.CharField(choices=[('EN', 'English'), ('PL', 'Polish'), ('ES', 'Spanish')], default='EN', max_length=3)),
                ('active', models.BooleanField()),
                ('color', models.CharField(choices=[('RED', 'Red'), ('WHITE', 'White'), ('BLUE', 'Blue'), ('BLACK', 'Black')], default='WHITE', max_length=5)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('host_url', models.URLField(blank=True)),
            ],
        ),
    ]
