# Generated by Django 5.0.4 on 2024-04-15 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=1)),
                ('total_number', models.PositiveIntegerField()),
                ('buy_now', models.IntegerField()),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('marka', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(default=0)),
                ('year', models.SmallIntegerField(default=0)),
                ('mileage', models.PositiveIntegerField(default=0)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('with_photo', models.BooleanField(default=False)),
                ('color', models.CharField(max_length=100)),
                ('volume', models.FloatField(default=0.0)),
            ],
        ),
    ]
