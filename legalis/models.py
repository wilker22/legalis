# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Operation(models.Model):
    """
    Esse modelo define as atuações do escritório
    em questão. Os campos são:

    .. attribute:: name
       Nome da Atuação

    .. attribute:: description
       Descrição da Atuação
    """
    name = models.CharField(_(u"Atuação"), max_length=90)
    description = models.TextField(_(u"Descrição"))

    class Meta:
        db_table = "operations"

    def __unicode__(self):
        return self.name
