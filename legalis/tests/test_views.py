# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from model_mommy import mommy


class LegalisPageTest(TestCase):

    """
    Testa o uso das flatpages
    """

    def setUp(self):
        site = Site.objects.get_current()
        self.page = FlatPage.objects.create(
            url="/about/",
            title="About",
            content="About content test",
            enable_comments=False,
            template_name="about.html",
            registration_required=False
        )
        self.page.sites.add(site)
        self.page.save()

        # Request page
        self.resp = self.client.get(reverse('flatpages',
                                    kwargs={'url': self.page.url}))

    def test_get(self):
        """GET /about/ deve retornar status 200"""
        self.assertEqual(200, self.resp.status_code)


class OperationViewTest(TestCase):

    """
    Testa a lista de atuações do escritório
    """

    def setUp(self):
        self.resp = self.client.get('/atuacoes/')

    def test_get(self):
        """GET /atuacoes/ deve retornar status 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Deve renderizar o template operation_list.html"""
        self.assertTemplateUsed(self.resp, 'operations/operations_list.html')


