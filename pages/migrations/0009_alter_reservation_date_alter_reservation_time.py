# Generated by Django 5.0 on 2023-12-22 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_reservation_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]
