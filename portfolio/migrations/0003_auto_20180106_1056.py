# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20180104_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
