# Generated by Django 5.0.2 on 2025-01-05 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventregistration',
            old_name='registration_date',
            new_name='registered_at',
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default=34, upload_to='event_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
