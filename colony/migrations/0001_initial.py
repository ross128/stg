# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('build_time', models.DurationField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BuildingAssignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('building', models.ForeignKey(to='colony.Building')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BuildingConstruction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('building', models.ForeignKey(to='colony.Building')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Colony',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Colonies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FieldAssignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.PositiveSmallIntegerField()),
                ('y', models.PositiveSmallIntegerField()),
                ('colony', models.ForeignKey(to='colony.Colony')),
                ('field', models.ForeignKey(to='colony.Field')),
            ],
            options={
                'ordering': ['y', 'x'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='fieldassignment',
            unique_together=set([('colony', 'x', 'y')]),
        ),
        migrations.AddField(
            model_name='colony',
            name='fields',
            field=models.ManyToManyField(to='colony.Field', through='colony.FieldAssignment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='colony',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buildingconstruction',
            name='field',
            field=models.ForeignKey(to='colony.Field'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='buildingassignment',
            name='field',
            field=models.ForeignKey(to='colony.FieldAssignment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='usable_fields',
            field=models.ManyToManyField(to='colony.Field', through='colony.BuildingConstruction'),
            preserve_default=True,
        ),
    ]
