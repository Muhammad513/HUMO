# Generated by Django 3.2.9 on 2023-04-22 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='activate',
            field=models.BooleanField(default=False),
        ),
    ]
