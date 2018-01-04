# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fund_type', models.CharField(max_length=32, choices=[(1, b'Crypto'), (2, b'Stock')])),
                ('date', models.DateTimeField(auto_now=True)),
                ('buying', models.DecimalField(max_digits=32, decimal_places=5)),
                ('redemption', models.DecimalField(max_digits=32, decimal_places=5)),
                ('dividends', models.DecimalField(max_digits=32, decimal_places=5)),
                ('total_injected', models.DecimalField(max_digits=32, decimal_places=5)),
                ('cash_balance', models.DecimalField(max_digits=32, decimal_places=5)),
                ('cost', models.DecimalField(max_digits=32, decimal_places=5)),
                ('market_value', models.DecimalField(max_digits=32, decimal_places=5)),
                ('total_asset', models.DecimalField(max_digits=32, decimal_places=5)),
                ('unrealized', models.DecimalField(max_digits=32, decimal_places=5)),
                ('per_unrealized', models.DecimalField(max_digits=32, decimal_places=5)),
                ('realized', models.DecimalField(max_digits=32, decimal_places=5)),
                ('cumul_realized', models.DecimalField(max_digits=32, decimal_places=5)),
                ('gross_nav', models.DecimalField(max_digits=32, decimal_places=5)),
                ('expenses', models.DecimalField(max_digits=32, decimal_places=5)),
                ('net_nav', models.DecimalField(max_digits=32, decimal_places=5)),
                ('shares', models.DecimalField(max_digits=32, decimal_places=5)),
                ('nav_share', models.DecimalField(max_digits=32, decimal_places=5)),
                ('per_variation', models.DecimalField(max_digits=32, decimal_places=5)),
                ('cumul_variation', models.DecimalField(max_digits=32, decimal_places=5)),
                ('set', models.DecimalField(max_digits=32, decimal_places=5)),
                ('set_var', models.DecimalField(max_digits=32, decimal_places=5)),
                ('note', models.CharField(max_length=1000)),
            ],
            options={
                'ordering': ('date', 'portfolio'),
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='fund',
            name='portfolio',
            field=models.ForeignKey(to='portfolio.Portfolio'),
        ),
        migrations.AddField(
            model_name='fund',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
