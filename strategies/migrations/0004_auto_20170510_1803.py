# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 15:03
from __future__ import unicode_literals

from django.db import migrations
import stdimage.models
import stdimage.utils


class Migration(migrations.Migration):

    dependencies = [
        ('strategies', '0003_auto_20170510_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steps',
            name='image',
            field=stdimage.models.StdImageField(upload_to=b'', verbose_name=stdimage.utils.UploadToClassNameDir()),
        ),
    ]
