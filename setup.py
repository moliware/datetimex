# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def requires():
  with open('requirements.txt') as fd:
    return list(map(lambda x: x.rstrip(), fd.readlines()))

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

setup(name='datetimex',
      version='0.0.1',
      description='Richer datetimes',
      long_description = open('README.rst').read(),
      author='Miguel Olivares',
      author_email='miguel@moliware.com',
      url='',
      packages=['datetimex'],
      install_requires=requires(),
      test_suite='tests',
      classifiers=CLASSIFIERS)
