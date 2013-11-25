# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


class Content(models.Model):
    """
    Classe base para todo o conteudo
    da aplicação.

    .. attribute:: created_at
       Data em que a página foi criada

    .. attribute:: updated_at
       Data em que a página foi atualizada
    """
    created_at = models.DateField(default=datetime.datetime.now(),
                                  editable=False)
    updated_at = models.DateField(default=datetime.datetime.now(),
                                  null=True,
                                  blank=True)

    class Meta:
        abstract = True


class PageBase(Content):
    """
    Classe base para os conteúdos de
    texto, como uma página.

    .. attribute: slug
       URL da Página

    .. attribute: title
       Título da Página

    .. attribute:: status
       Define o status da página como:

        - Rascunho;
        - Publicado.
    """

    # Status da Página
    DRAFT = 'D'
    PUBLISHED = 'P'
    STATUS_CHOICES = (
        (DRAFT, _(u'Rascunho')),
        (PUBLISHED, _(u'Publicado')),
    )

    slug = models.SlugField(_(u'URL'), unique=True)
    title = models.CharField(_(u'Título da Página'), max_length=100)
    status = models.CharField(_(u'Status'), max_length=1,
                              choices=STATUS_CHOICES)

    class Meta:
        abstract = True


# Signal responsável por gerar o slug antes de salvar
@receiver(pre_save, sender=PageBase)
def generate_slug(sender, **kwargs):
    """
    Gera o slug se o mesmo
    não foi preenchido.
    """
    import ipdb; ipdb.set_trace()
