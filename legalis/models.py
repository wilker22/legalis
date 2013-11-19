# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Operation(models.Model):
    name = models.CharField(_(u"Atuação"), max_length=90)
    description = models.TextField(_(u"Descrição"))

    class Meta:
        db_table = "operations"

    def __unicode__(self):
        return self.name
