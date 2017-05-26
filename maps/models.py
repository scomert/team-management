# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Map(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __unicode__(self):
        return self.name
