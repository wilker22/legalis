# -*- coding: utf-8 -*-

from django.test import TestCase

from legalis.models import Operation


class OperationModelTest(TestCase):
    def setUp(self):
        self.operation = Operation.objects.create(
            name="Direto Civil",
            description="Descricao do direito civil"
        )

    def test_create(self):
        """Deve criar a atuacao"""
        self.assertEqual(self.operation.pk, 1)
