#!/usr/bin/env python

import os
import sys
import multiprocessing

from django.conf import settings


EXTERNAL_MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

INTERNAL_MIDDLEWARE = []

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.flatpages',
]
INTERNAL_APPS = [
    'django_nose',
    'legalis',
]

if not settings.configured:
    settings.configure(
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        MIDDLEWARE_CLASSES = EXTERNAL_MIDDLEWARE + INTERNAL_MIDDLEWARE,
        INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS,
        ROOT_URLCONF='legalis.tests.urls',
        TEMPLATE_DIRS = (
            os.path.join(os.path.dirname(__file__), '../templates'),
        ),
        SITE_ID = 1,
        COVERAGE_MODULE_EXCLUDES = EXTERNAL_APPS,
        COVERAGE_REPORT_HTML_OUTPUT_DIR=os.path.join(os.path.dirname(__file__), 'coverage')
    )


from django_coverage.coverage_runner import CoverageRunner
from django_nose import NoseTestSuiteRunner

class NoseCoverageTestRunner(CoverageRunner, NoseTestSuiteRunner):
    pass

def runtests(*test_args):
    failures = NoseCoverageTestRunner(verbosity=2, interactive=True).run_tests(test_args)
    sys.exit(failures)

if __name__ == '__main__':
    runtests(*sys.argv[1:])

