# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20180121_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='fund_type',
            field=models.CharField(max_length=32),
        ),
    ]
