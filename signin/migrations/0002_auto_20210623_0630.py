# Generated by Django 3.2.4 on 2021-06-23 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='name',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='password',
        ),
    ]
