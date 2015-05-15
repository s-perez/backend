# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Topics', '0001_initial'),
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='topics',
            field=models.ManyToManyField(related_name='accounts', to='Topics.Topic'),
        ),
    ]
