# Generated by Django 3.2.15 on 2023-08-29 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_message_message_tweet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('description', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.message')),
            ],
        ),
    ]