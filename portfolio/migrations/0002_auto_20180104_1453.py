# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='fund_type',
            field=models.CharField(max_length=32, choices=[(b'crypto', b'Crypto'), (b'stocks', b'Stock')]),
        ),
    ]
