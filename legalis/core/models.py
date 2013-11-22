# -*- coding: utf-8 -*-
import datetime

from django.db import models


class Content(models.Model):
    created_at = models.DateField(default=datetime.datetime.now())
    updated_at = models.DateField(default=datetime.datetime.now())
