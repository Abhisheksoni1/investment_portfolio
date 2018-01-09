# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20180106_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='cumul_realized',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='fund',
            name='cumul_variation',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='fund',
            name='gross_nav',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='fund',
            name='nav_share',
            field=models.DecimalField(default=1, max_digits=32, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='fund',
            name='net_nav',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='fund',
            name='per_unrealized',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='fund',
            name='per_variation',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='fund',
            name='realized',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='fund',
            name='set_var',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='fund',
            name='shares',
            field=models.DecimalField(default=1, max_digits=32, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='fund',
            name='total_asset',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='fund',
            name='total_injected',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='fund',
            name='unrealized',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=5),
        ),
    ]
