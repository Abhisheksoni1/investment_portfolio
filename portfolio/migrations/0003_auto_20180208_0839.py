# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20180201_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='buying',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='cash_balance',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='cost',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='cumul_realized',
            field=models.DecimalField(max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='cumul_variation',
            field=models.DecimalField(max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='dividends',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='expenses',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='gross_nav',
            field=models.DecimalField(max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='market_value',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='nav_share',
            field=models.DecimalField(max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='net_nav',
            field=models.DecimalField(max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='per_unrealized',
            field=models.DecimalField(max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='per_variation',
            field=models.DecimalField(max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='realized',
            field=models.DecimalField(max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='redemption',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='set',
            field=models.DecimalField(default=0, max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='set_var',
            field=models.DecimalField(max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='shares',
            field=models.DecimalField(max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='total_asset',
            field=models.DecimalField(max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='total_injected',
            field=models.DecimalField(max_digits=32, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='fund',
            name='unrealized',
            field=models.DecimalField(max_digits=32, decimal_places=3),
        ),
    ]
