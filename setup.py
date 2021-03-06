#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'importlab'
DESCRIPTION = 'A tool to run static analysis over large python projects.'
URL = 'https://github.com/google/importlab'
EMAIL = 'pytype-dev@google.com'
AUTHOR = 'Google Inc.'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1'

REQUIRED = [
    'networkx'
]

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

PACKAGES=find_packages(exclude=('tests',))

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    maintainer=AUTHOR,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=PACKAGES,
    scripts=['bin/importlab'],
    install_requires=REQUIRED,
    include_package_data=True,
    license='Apache 2.0',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
