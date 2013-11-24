# -*- coding: utf-8 -*-
import datetime

from django.db import models
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


    def save(self, commit=True):
        page = super(PageBase, self).save(commit=False)

        # Se o slug não foi preenchido, então cria um novo
        if page.slug:
            page._generate_slug()

        if commit:
            page.save()
        return page

    def _generate_slug(self):
        """
        Gera o slug se o mesmo
        não foi preenchido.
        """
        self.slug = slugify(self.title)

    class Meta:
        abstract = True
