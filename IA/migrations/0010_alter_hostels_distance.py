# Generated by Django 4.1.2 on 2023-02-27 22:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IA', '0009_hostels_price_per_night_hostels_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostels',
            name='distance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
