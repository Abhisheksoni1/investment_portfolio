# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20180113_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='note',
            field=models.CharField(max_length=1000, blank=True),
        ),
    ]
