# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('colony', '0002_django_duration_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingassignment',
            name='construction_finished',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
