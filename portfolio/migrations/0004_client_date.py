# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20180208_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 8, 9, 56, 22, 726048, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
