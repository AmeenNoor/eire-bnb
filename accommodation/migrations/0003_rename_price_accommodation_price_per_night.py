# Generated by Django 3.2.23 on 2024-01-02 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0002_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accommodation',
            old_name='price',
            new_name='price_per_night',
        ),
    ]
