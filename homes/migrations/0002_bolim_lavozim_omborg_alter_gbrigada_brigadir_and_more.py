# Generated by Django 4.1.7 on 2023-04-13 12:16

from django.db import migrations, models
import django.db.models.deletion
import homes.models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bolim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bolim', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lavozim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lavozim', models.CharField(max_length=30)),
            ],
        ),
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
            name='Hodim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('jshir', models.CharField(max_length=14)),
                ('pasport', models.CharField(blank=True, max_length=9, null=True)),
                ('pic', models.ImageField(default='default/avatar.png', upload_to=homes.models.get_image_path)),
                ('bolim', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='homes.bolim')),
                ('lavozim', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='homes.lavozim')),
            ],
        ),
        migrations.CreateModel(
            name='Galla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('yuk_num', models.CharField(max_length=3)),
                ('tr_marka', models.CharField(choices=[('ЗИЛ', 'ЗИЛ'), ('КАМАЗ', 'КАМАЗ'), ('БОШКА', 'БОШКА')], max_length=20)),
                ('tr_num', models.CharField(max_length=20)),
                ('tr_name', models.CharField(max_length=30)),
                ('imzo', models.BooleanField(default=False)),
                ('brutto', models.FloatField(blank=True, null=True)),
                ('tara', models.FloatField(blank=True, null=True)),
                ('sofVazn', models.IntegerField(blank=True, default=0, null=True)),
                ('brigada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homes.gbrigada')),
                ('ombor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homes.omborg')),
            ],
        ),
    ]
