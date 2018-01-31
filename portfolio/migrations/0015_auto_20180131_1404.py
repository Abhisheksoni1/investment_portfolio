# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_client_investor'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='fund',
            name='fund_type',
            field=models.CharField(max_length=32, choices=[('crypto', 'Crypto'), ('stocks', 'Stock')]),
        ),
    ]
