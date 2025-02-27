# Generated by Django 5.0.2 on 2025-01-05 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='meal_option',
            field=models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner'), ('A', 'All')], default=False, max_length=1),
        ),
    ]
