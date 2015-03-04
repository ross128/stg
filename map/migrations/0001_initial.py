# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FieldType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='field',
            name='fieldtype',
            field=models.ForeignKey(to='map.FieldType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='field',
            unique_together=set([('x', 'y')]),
        ),
        migrations.AlterIndexTogether(
            name='field',
            index_together=set([('x', 'y')]),
        ),
    ]
