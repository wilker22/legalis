# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

import legalis


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='legalis',
    version=legalis.__version__,
    description='Gerenciador de Conteúdo (CMS) especializado para escritórios de advocacia.',
    long_description=read('README.rst'),
    license='MIT License',
    author='Gilson Filho',
    author_email='contato@gilsondev.com',
    url='https://github.com/legalis/legalis',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django==1.5.1',
        'South==0.8.2',
        'Unipath==1.0',
        'dj-database-url==0.2.2',
        'django-widget-tweaks==1.3',
        'rednose==0.4.0'
    ],
    tests_require=[
        'Django',
        'django-nose',
        'coverage',
        'django-coverage',
        'model-mommy'
    ],
    test_suite='legalis.tests.runtests.runtests',
)
