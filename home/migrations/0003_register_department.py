# Generated by Django 5.0.2 on 2024-11-08 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_register_set_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='department',
            field=models.CharField(default='sbcsdbcpWBDC', max_length=50),
            preserve_default=False,
        ),
    ]
