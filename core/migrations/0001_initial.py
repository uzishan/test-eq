# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=255)),
                ('location_address', models.CharField(max_length=100)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('title', models.CharField(max_length=30)),
                ('plans_image_url', models.CharField(max_length=255)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('surface', models.CharField(max_length=30)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Floor')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('serial_no', models.IntegerField()),
                ('type', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('unit_of_measurement', models.CharField(max_length=10)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Room')),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name=b'Read date')),
                ('value', models.IntegerField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Sensor')),
            ],
        ),
    ]
