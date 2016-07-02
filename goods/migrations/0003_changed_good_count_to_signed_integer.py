# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_changed_good_count_to_positive_integer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodassignment',
            name='count',
            field=models.IntegerField(),
        ),
    ]
