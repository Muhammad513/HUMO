# Generated by Django 4.1.7 on 2023-04-07 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OmborG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('reja', models.FloatField(null=True)),
                ('sentner', models.FloatField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='gbrigada',
            name='brigadir',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='hudud',
            name='h_num',
            field=models.CharField(max_length=1),
        ),
        migrations.CreateModel(
            name='Galla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('sofVazn', models.IntegerField(blank=True)),
                ('yuk_num', models.CharField(blank=True, max_length=3)),
                ('tr_marka', models.CharField(blank=True, choices=[('ЗИЛ', 'ЗИЛ'), ('КАМАЗ', 'КАМАЗ'), ('БОШКА', 'БОШКА')], max_length=20)),
                ('tr_num', models.CharField(blank=True, max_length=20)),
                ('tr_name', models.CharField(blank=True, max_length=30, null=True)),
                ('imzo', models.BooleanField(default=False)),
                ('brigada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='homes.gbrigada')),
                ('ombor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='homes.omborg')),
            ],
        ),
    ]