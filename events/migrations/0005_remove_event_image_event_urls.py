# Generated by Django 5.0.2 on 2025-01-08 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.AddField(
            model_name='event',
            name='urls',
            field=models.CharField(default=6, max_length=500),
            preserve_default=False,
        ),
    ]
