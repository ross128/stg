# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GoodAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('count', models.IntegerField()),
                ('good', models.ForeignKey(to='goods.Good')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('goods', models.ManyToManyField(to='goods.Good', through='goods.GoodAssignment')),
            ],
        ),
        migrations.AddField(
            model_name='goodassignment',
            name='stock',
            field=models.ForeignKey(to='goods.Stock'),
        ),
        migrations.AlterUniqueTogether(
            name='goodassignment',
            unique_together=set([('stock', 'good')]),
        ),
    ]
