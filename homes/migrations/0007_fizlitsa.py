# Generated by Django 4.1.7 on 2023-04-30 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0006_remove_hodim_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fizlitsa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('ful_name', models.CharField(max_length=50)),
                ('birth', models.DateField()),
            ],
        ),
    ]