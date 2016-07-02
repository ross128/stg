# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from goods.models import Stock

def insertDefaultStockIDs(apps, schema_editor):
    """inserts the default stock IDs for the newly created OneToOneField"""
    Building = apps.get_model("colony", "Building")
    for building in Building.objects.all():
        stock = Stock.objects.create()
        stock.save()
        building.building_cost_id = stock.pk
        building.save()

class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_changed_good_count_to_positive_integer'),
        ('colony', '0002_colony_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='building_cost',
            field=models.OneToOneField(to='goods.Stock', null=True),
            preserve_default=False,
        ),
        migrations.RunPython(insertDefaultStockIDs, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='building',
            name='building_cost',
            field=models.OneToOneField(to='goods.Stock', null=False),
        ),
    ]
