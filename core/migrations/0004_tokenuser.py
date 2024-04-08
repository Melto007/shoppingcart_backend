# Generated by Django 3.2 on 2024-04-08 12:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20240407_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(blank=True, null=True)),
                ('token', models.CharField(blank=True, max_length=255, null=True)),
                ('expired_at', models.DateTimeField(default=datetime.datetime(2024, 4, 15, 12, 23, 31, 800521))),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]