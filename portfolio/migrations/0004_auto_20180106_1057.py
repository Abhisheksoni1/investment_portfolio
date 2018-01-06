# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20180106_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
