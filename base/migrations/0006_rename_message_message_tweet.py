# Generated by Django 3.2.15 on 2023-08-28 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_user_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='tweet',
        ),
    ]
