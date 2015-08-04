# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ships', '0002_auto_20150302_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ModuleAssignment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('count', models.PositiveSmallIntegerField()),
                ('module', models.ForeignKey(to='ships.Module')),
                ('ship', models.ForeignKey(to='ships.Ship')),
            ],
        ),
        migrations.AddField(
            model_name='ship',
            name='modules',
            field=models.ManyToManyField(through='ships.ModuleAssignment', to='ships.Module'),
        ),
        migrations.AlterUniqueTogether(
            name='moduleassignment',
            unique_together=set([('ship', 'module')]),
        ),
    ]
