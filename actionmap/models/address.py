# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Address(models.Model):
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    last_edit = models.DateTimeField(auto_now=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{}, {}, {}, {}".format(self.lat, self.lng, self.address, self.added_on)
