# -*- coding: utf-8 -*-

import os
from setuptools import setup

import legalis

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

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

try:
    long_description = open('README.rst').read()
except:
    long_description = legalis.__description__

setup(
    name='legalis',
    version=legalis.__version__,
    packages=['legalis'],
    include_package_data=True,
    license=legalis.__license__,
    description=legalis.__description__,
    long_description=long_description,
    url='http://github.com/legalis/legalis',
    download_url="https://github.com/legalis/legalis/tarball/master",
    namespace_packages=['legalis'],
    package_dir={'legalis': 'legalis'},
    install_requires=REQUIREMENTS,
    author=legalis.__author__,
    author_email=legalis.__email__,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords='legalis cms django apps websites',
)
