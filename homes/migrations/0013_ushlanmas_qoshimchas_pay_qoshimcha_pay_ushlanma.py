# Generated by Django 4.1.7 on 2023-05-21 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0012_remove_pay_qoshimcha_remove_pay_sum1_remove_pay_sum2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UshlanmaS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sums', models.FloatField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homes.ushlanma')),
            ],
        ),
        migrations.CreateModel(
            name='QoshimchaS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sums', models.FloatField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homes.qoshimcha')),
            ],
        ),
        migrations.AddField(
            model_name='pay',
            name='qoshimcha',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='homes.qoshimchas'),
        ),
        migrations.AddField(
            model_name='pay',
            name='ushlanma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='homes.ushlanmas'),
        ),
    ]
