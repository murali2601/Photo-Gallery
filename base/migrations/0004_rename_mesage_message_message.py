# Generated by Django 3.2.15 on 2023-08-28 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20230828_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='mesage',
            new_name='message',
        ),
    ]
