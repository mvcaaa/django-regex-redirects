# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-regex-redirects',
    version='0.0.3',
    author=u'Alex de Landgraaf, Andrey Astashov',
    author_email='alex@maykinmedia.nl, mvc.aaa@gmail.com',
    packages=find_packages(),
    url='https://github.com/maykinmedia/django-regex-redirects',
    license='BSD licence, see LICENCE.txt',
    description='Django redirects, with regular expressions',
    include_package_data=True,
)
