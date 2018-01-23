# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_auto_20180121_0705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='name',
        ),
    ]
