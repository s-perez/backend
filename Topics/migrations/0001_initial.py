# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length='200')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_written', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(to='Topics.Feed', related_name='news')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_access', models.DateTimeField(auto_now_add=True)),
                ('feeds', models.ManyToManyField(related_name='topics', to='Topics.Feed')),
            ],
        ),
    ]
