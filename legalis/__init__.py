#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pkg_resources

pkg_resources.declare_namespace(__name__)

VERSION = (0, 0, 1)

LEGALIS_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.redirects',
    'django.contrib.flatpages',

    'legalis.core',
    'legalis.procedure',
]

__version__ = ".".join(map(str, VERSION))
__status__ = "Development"
__description__ = u"Gerenciador de Conteúdo (CMS) baseado no Projeto Opps, especializado para escritórios de advocacia."

__author__ = u"Gilson Filho"
__email__ = u"legalis.cms@gmail.com"
__license__ = u"MIT License"
__copyright__ = u"Copyright 2013, Legalis Project"
