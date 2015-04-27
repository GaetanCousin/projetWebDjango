# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20150424_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviestate',
            name='view',
        ),
    ]
