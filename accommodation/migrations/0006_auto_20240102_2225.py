# Generated by Django 3.2.23 on 2024-01-02 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0005_auto_20240102_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out_date',
            field=models.DateField(),
        ),
    ]
