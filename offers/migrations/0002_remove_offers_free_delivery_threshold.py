# Generated by Django 3.2 on 2023-02-22 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offers',
            name='free_delivery_threshold',
        ),
    ]