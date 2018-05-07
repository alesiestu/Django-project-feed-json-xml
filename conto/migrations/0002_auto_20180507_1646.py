# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='info',
            field=models.CharField(max_length=40),
        ),
    ]
