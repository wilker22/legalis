#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include

urlpatterns = patterns('',

)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^(?P<url>.*/)$', 'flatpage', name='flatpages'),
)
