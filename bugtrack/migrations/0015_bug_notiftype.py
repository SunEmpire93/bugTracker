# Generated by Django 3.0.8 on 2020-08-29 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtrack', '0014_user_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='notifType',
            field=models.CharField(blank=True, default='none', max_length=50, null=True),
        ),
    ]
