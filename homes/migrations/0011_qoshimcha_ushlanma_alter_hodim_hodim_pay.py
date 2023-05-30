# Generated by Django 4.1.7 on 2023-05-21 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_remove_profile_hodim'),
        ('homes', '0010_hodim_hodim'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qoshimcha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ushlanma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='hodim',
            name='hodim',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='login.profile'),
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oylik', models.FloatField()),
                ('sum1', models.FloatField(default=0)),
                ('sum2', models.FloatField(default=0)),
                ('soliq', models.FloatField(default=0)),
                ('plastik', models.FloatField()),
                ('date', models.DateField()),
                ('hodim', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homes.hodim')),
                ('qoshimcha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homes.qoshimcha')),
                ('ushlanma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homes.ushlanma')),
            ],
        ),
    ]