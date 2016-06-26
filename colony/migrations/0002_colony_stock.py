# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from goods.models import Stock

def insertDefaultStockIDs(apps, schema_editor):
    """inserts the default stock IDs for the newly created OneToOneField"""
    Colony = apps.get_model("colony", "Colony")
    for colony in Colony.objects.all():
        stock = Stock.objects.create()
        stock.save()
        colony.stock_id = stock.pk
        colony.save()

class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
        ('colony', '0001_squashed_0004_use_django_datetime_in_construction_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='colony',
            name='stock',
            field=models.OneToOneField(to='goods.Stock', null=True),
            preserve_default=False,
        ),
        migrations.RunPython(insertDefaultStockIDs, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='colony',
            name='stock',
            field=models.OneToOneField(to='goods.Stock', null=False),
        ),
    ]
