# -*- coding: utf-8 -*-

from django.test import TestCase

from legalis.core.models import Content, PageBase

class HomepageTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        """GET / deve retornar status 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Homepage deve usar o template index.html"""
        self.assertTemplateUsed(self.resp, 'core/index.html')


class ContentModelTestCase(TestCase):

    def setUp(self):
        self.fields = Content._meta.get_all_field_names()

    def test_should_created_at_field(self):
        """Verifica se o modelo tem o created_at"""
        self.assertIn("created_at", self.fields)

    def test_should_updates_at_field(self):
        self.fields
        self.assertIn("updated_at", self.fields)


class PageBaseModelTest(TestCase):

    def setUp(self):
        self.fields = PageBase._meta.get_all_field_names()

    def test_should_slug(self):
        """Verifica se o modelo tem o slug"""
        self.assertIn("slug", self.fields)

    def test_should_generate_slug(self):
        """Deve gerar o slug baseado no titulo"""

        # Criando classe baseado no PageBase
        class PageTest(PageBase):
            pass

        self.flatpage = PageTest.objects.create(
            title="FlatPage with Slug"
        )

        self.assertEqual(self.flatpage.slug, "flatpage-with-slug")
