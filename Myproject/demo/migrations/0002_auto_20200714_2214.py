# Generated by Django 3.0.8 on 2020-07-14 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='Events',
        ),
        migrations.RenameModel(
            old_name='Menu',
            new_name='Menus',
        ),
    ]
