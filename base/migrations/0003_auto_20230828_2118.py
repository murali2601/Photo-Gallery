# Generated by Django 3.2.15 on 2023-08-28 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20230828_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='time',
        ),
        migrations.AddField(
            model_name='message',
            name='mesage',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.user'),
        ),
    ]
