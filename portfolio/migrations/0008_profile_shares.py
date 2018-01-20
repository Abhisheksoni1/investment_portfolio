# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20180119_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='shares',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=4),
        ),
    ]
