# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from legalis.core.models import PageBase


class FlatPage(PageBase):
    """
    Toda a estrutura de uma página estática,
    está aqui.

    .. attribute:: body
       Corpo da Página
    """
    body = models.TextField(_(u'Conteúdo da Página'))

