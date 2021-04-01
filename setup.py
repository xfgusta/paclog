#!/usr/bin/python

from setuptools import setup

LONG_DESCRIPTION = '''
# paclog

A pacman log analyzer

# License

The MIT License (MIT)

paclog 2.0 Copyright (C) 2021 Gustavo Costa
'''

setup(name='paclog',
      version='2.0',
      description='A pacman log analyzer',
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      author='Gustavo Costa',
      author_email='xfgusta@gmail.com',
      url='https://github.com/xfgusta/paclog/',
      scripts=['paclog'],
)
