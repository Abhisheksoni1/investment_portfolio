# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_client_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('date',)},
        ),
    ]
