# Generated by Django 3.0.8 on 2020-07-30 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtrack', '0004_bug_fix'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solver',
            name='updates',
        ),
        migrations.AddField(
            model_name='bug',
            name='updates',
            field=models.ManyToManyField(related_name='bugUpdate', to='bugtrack.Update'),
        ),
    ]