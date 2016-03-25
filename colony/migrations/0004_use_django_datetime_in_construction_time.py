# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('colony', '0003_building_construction_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingassignment',
            name='construction_finished',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
