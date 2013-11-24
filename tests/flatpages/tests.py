# -*- coding: utf-8 -*-

from django.test import TestCase

from legalis.flatpages.models import FlatPage


class FlatPageModelTest(TestCase):

    def test_should_body_field(self):
        """Verifica se o modelo tem o campo body"""
        fields = FlatPage._meta.get_all_field_names()
        self.assertIn("body", fields)

    def test_should_created_at_save(self):
        """Deve ser registrado a data de criação"""
        self.flatpage = FlatPage.objects.create(
            title="Flatpage Test",
            slug="flatpage-test",
            body="Body TestPage"
        )

        self.assertEqual(self.flatpage.pk, 1)
