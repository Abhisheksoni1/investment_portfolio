# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_auto_20180131_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='fund_type',
            field=models.CharField(max_length=32),
        ),
    ]
