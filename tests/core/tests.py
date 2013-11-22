# -*- coding: utf-8 -*-

from django.test import TestCase

from legalis.core.models import Content


class ProdutoModelTestCase(TestCase):
    def setUp(self):
        self.fields = Content._meta.get_all_field_names()


    def test_should_created_at_field(self):
        """Should take created_at in model"""
        self.assertIn("created_at", self.fields)

    def test_should_updates_at_field(self):
        """Should take updates_at in model"""
        self.assertIn("updated_at", self.fields)
