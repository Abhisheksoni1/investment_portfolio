# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_auto_20180121_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(default=b'Ram', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='nav',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=4),
        ),
        migrations.AddField(
            model_name='client',
            name='value',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=4),
        ),
    ]
