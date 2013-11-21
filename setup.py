#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

import legalis

REQUIREMENTS = [
    'Django==1.5.1',
    'South==0.8.2',
    'Unipath==1.0',
    'dj-database-url==0.2.2',
    'django-widget-tweaks==1.3',
    'rednose==0.4.0'
]

REQUIREMENTS_TEST = [
    'Django',
    'django-nose',
    'coverage',
    'django-coverage',
    'model-mommy'
]


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Framework :: Django",
    'Programming Language :: Python',
    "Programming Language :: Python :: 2.7",
    "Operating System :: OS Independent",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules']

try:
    long_description = open('README.rst').read()
except:
    long_description = legalis.__description__

setup(name='legalis',
      version=legalis.__version__,
      description=legalis.__description__,
      long_description=long_description,
      classifiers=classifiers,
      keywords='legalis cms django apps websites',
      author=legalis.__author__,
      author_email=legalis.__email__,
      url='https://github.com/legalis/legalis',
      download_url="https://github.com/legalis/legalis/tarball/master",
      license=legalis.__license__,
      packages=find_packages(exclude=('doc', 'docs', 'example')),
      namespace_packages=['legalis'],
      package_dir={'legalis': 'legalis'},
      install_requires=REQUIREMENTS,
      scripts=['legalis/bin/opps-admin.py'],
      include_package_data=True,
      test_suite='runtests')
