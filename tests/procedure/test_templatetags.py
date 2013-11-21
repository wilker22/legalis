# -*- coding: utf-8 -*-

from django.test import TestCase
from django.template import Template, Context, TemplateSyntaxError

from model_mommy import mommy


class ProcedureListTemplateTagTest(TestCase):

    def setUp(self):
        mommy.make('procedure.Procedure', name="Test")

    def test_list_tag(self):
        """Renderiza a lista de atuacoes"""
        out = Template(
            "{% load procedure %}"
            "{% procedure_list %}"
        ).render(Context())

        # FIXME: Ver uma forma de comparar o conteudo renderizado
