# -*- coding: utf-8 -*-

from django.test import TestCase

from legalis.models import Operation


class OperationModelTest(TestCase):
    def setUp(self):
        self.operation = Operation.objects.create(
            name="Direito Civil",
            description="Descricao do direito civil"
        )

    def test_create(self):
        """Deve criar a atuacao"""
        self.assertEqual(self.operation.pk, 1)

    def test_unicode(self):
        """Retorna a representacao do objeto"""
        self.assertEquals(unicode(self.operation), u"Direito Civil")
