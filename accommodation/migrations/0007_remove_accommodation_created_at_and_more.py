# Generated by Django 5.0.2 on 2025-03-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0006_alter_accommodation_meal_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accommodation',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='accommodation',
            name='meal_option',
        ),
        migrations.RemoveField(
            model_name='accommodation',
            name='user',
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='hostel_required',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3),
        ),
    ]
