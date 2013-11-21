# -*- coding: utf-8 -*-

from django.test import TestCase

from legalis.procedure.models import Procedure


class ProcedureModelTest(TestCase):
    def setUp(self):
        self.procedure = Procedure.objects.create(
            name="Direito Civil",
            description="Descricao do direito civil"
        )

    def test_create(self):
        """Deve criar a atuacao"""
        self.assertEqual(self.procedure.pk, 1)

    def test_unicode(self):
        """Retorna a representacao do objeto"""
        self.assertEquals(unicode(self.procedure), u"Direito Civil")
