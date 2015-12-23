# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='domain',
            field=models.CharField(default='internet', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='sub_title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
