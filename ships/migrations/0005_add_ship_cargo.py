# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from goods.models import Stock

def insertDefaultCargoIDs(apps, schema_editor):
    """inserts the default stock IDs for the newly created OneToOneField"""
    Ship = apps.get_model("ships", "Ship")
    for ship in Ship.objects.all():
        cargo = Stock.objects.create()
        cargo.save()
        ship.cargo_id = cargo.pk
        ship.save()

class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
        ('ships', '0004_module_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='cargo',
            field=models.OneToOneField(to='goods.Stock', null=True),
            preserve_default=False,
        ),
        migrations.RunPython(insertDefaultCargoIDs, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='ship',
            name='cargo',
            field=models.OneToOneField(to='goods.Stock', null=False),
        ),

    ]
