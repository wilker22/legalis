# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.simple_tag
def active_page(request, view_name):
    from django.core.urlresolvers import reverse, Resolver404
    if not request:
        return ""
    if view_name == '':
        return ""
    try:
        return "active" if reverse(view_name) == request.path_info else ""
    except Resolver404:
        return ""
