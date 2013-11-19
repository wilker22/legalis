# -*- coding: utf-8 -*-

from django.test import TestCase
from django.template import Template, Context, TemplateSyntaxError

from model_mommy import mommy


class OperationListTemplateTagTest(TestCase):

    def setUp(self):
        mommy.make('legalis.Operation', name="Test")

    def test_list_tag(self):
        """Renderiza a lista de atuacoes"""
        out = Template(
            "{% load operations %}"
            "{% operation_list %}"
        ).render(Context())

        # FIXME: Ver uma forma de comparar o conteudo renderizado
