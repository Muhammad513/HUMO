# Generated by Django 4.1.7 on 2023-05-31 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0019_hodim_pays'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hodim',
            name='pays',
        ),
    ]
