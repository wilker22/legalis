# -*- coding: utf-8 -*-

from django.views.generic import TemplateView


class HomepageView(TemplateView):

    """Homepage do site"""
    template_name = "index.html"
