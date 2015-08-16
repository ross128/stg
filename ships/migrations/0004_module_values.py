# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0003_ship_modules'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModulePropertyAssignment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('value', models.FloatField()),
                ('module', models.ForeignKey(to='ships.Module')),
            ],
        ),
        migrations.CreateModel(
            name='ShipProperty',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='shipclass',
            options={'verbose_name_plural': 'Ship classes'},
        ),
        migrations.AddField(
            model_name='modulepropertyassignment',
            name='module_property',
            field=models.ForeignKey(to='ships.ShipProperty'),
        ),
        migrations.AddField(
            model_name='module',
            name='module_properties',
            field=models.ManyToManyField(to='ships.ShipProperty', through='ships.ModulePropertyAssignment'),
        ),
        migrations.AlterUniqueTogether(
            name='modulepropertyassignment',
            unique_together=set([('module', 'module_property')]),
        ),
    ]
