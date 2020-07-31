# Generated by Django 3.0.8 on 2020-07-30 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtrack', '0007_bug_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bug',
            name='fix',
        ),
        migrations.AddField(
            model_name='bug',
            name='fixed',
            field=models.BooleanField(default=False),
        ),
    ]
