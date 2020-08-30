# Generated by Django 2.2.13 on 2020-08-29 18:04

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('curr_employment', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('links', django_mysql.models.JSONField(default=dict)),
                ('skills', django_mysql.models.JSONField(default=dict)),
                ('hobbies', django_mysql.models.JSONField(default=dict)),
                ('profile', models.CharField(max_length=2000)),
                ('employment_hist', django_mysql.models.JSONField(default=dict)),
                ('education', django_mysql.models.JSONField(default=dict)),
                ('references', django_mysql.models.JSONField(default=dict)),
            ],
        ),
    ]
