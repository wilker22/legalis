# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from model_mommy import mommy


class LegalisAboutPageTest(TestCase):
    """
    Verify the pages:

        - About;
        - Office;
        - Performance;
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
        self.resp = self.client.get(self.page.url)

    def test_get(self):
        """GET /about/ should return 200 status code"""
        self.assertEqual(200, self.resp.status_code)
