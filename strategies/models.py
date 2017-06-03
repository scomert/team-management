# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from stdimage import StdImageField
from stdimage.utils import UploadToClassNameDir

from maps.models import Map
from django.contrib.auth.models import User
from stdimage.utils import UploadToUUID


# Create your models here.

def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "%s/%s" % (instance.id, filename)


class Strategy(models.Model):
    name = models.CharField(default="", blank=False, null=False, max_length=100)
    map = models.ForeignKey(Map)

    def __unicode__(self):
        return self.name


class Steps(models.Model):
    command = models.TextField()
    image = StdImageField(UploadToClassNameDir(), upload_to=UploadToUUID(path='images'), variations={'thumbnail': {'width': 480, 'height': 360},
                                                              'oyun': {'width': 640, 'height': 480},
                                                              'buyuk_oyun': {'width': 800, 'height': 600}})
    strategy = models.ForeignKey(Strategy)
    user = models.ForeignKey(User, default=0)
    priority = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.command
