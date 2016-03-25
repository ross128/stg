# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import timedelta.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [('colony', '0001_initial'), ('colony', '0002_django_duration_field'), ('colony', '0003_building_construction_timestamp'), ('colony', '0004_use_django_datetime_in_construction_time')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('build_time', timedelta.fields.TimedeltaField()),
            ],
        ),
        migrations.CreateModel(
            name='BuildingAssignment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('building', models.ForeignKey(to='colony.Building')),
            ],
        ),
        migrations.CreateModel(
            name='BuildingConstruction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('building', models.ForeignKey(to='colony.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Colony',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Colonies',
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FieldAssignment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('x', models.PositiveSmallIntegerField()),
                ('y', models.PositiveSmallIntegerField()),
                ('colony', models.ForeignKey(to='colony.Colony')),
                ('field', models.ForeignKey(to='colony.Field')),
            ],
            options={
                'ordering': ['y', 'x'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='fieldassignment',
            unique_together=set([('colony', 'x', 'y')]),
        ),
        migrations.AddField(
            model_name='colony',
            name='fields',
            field=models.ManyToManyField(through='colony.FieldAssignment', to='colony.Field'),
        ),
        migrations.AddField(
            model_name='colony',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='buildingconstruction',
            name='field',
            field=models.ForeignKey(to='colony.Field'),
        ),
        migrations.AddField(
            model_name='buildingassignment',
            name='field',
            field=models.ForeignKey(to='colony.FieldAssignment'),
        ),
        migrations.AddField(
            model_name='building',
            name='usable_fields',
            field=models.ManyToManyField(through='colony.BuildingConstruction', to='colony.Field'),
        ),
        migrations.AlterField(
            model_name='building',
            name='build_time',
            field=models.DurationField(),
        ),
        migrations.AddField(
            model_name='buildingassignment',
            name='construction_finished',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
