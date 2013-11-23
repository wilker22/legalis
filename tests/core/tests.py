# -*- coding: utf-8 -*-

from django.test import TestCase

from legalis.core.models import Content


class ContentModelTestCase(TestCase):

    def setUp(self):
        self.fields = Content._meta.get_all_field_names()

    def test_should_created_at_field(self):
        """Verifica se o modelo tem o created_at"""
        self.assertIn("created_at", self.fields)

    def test_should_updates_at_field(self):
        """Verifica se o modelo tem o updated_at"""
        self.assertIn("updated_at", self.fields)
