# Generated by Django 4.1.7 on 2023-04-23 08:32

from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_profile_activate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='default/avatar.jpg', upload_to=login.models.get_image_path),
        ),
    ]