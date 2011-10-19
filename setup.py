#!/usr/bin/env python

from setuptools import setup
import sys

PACKAGE_PATH = 'src'

sys.path.insert(0, PACKAGE_PATH)
import pydir

setup(
    name='pydir',
    version=pydir.version_string(),
    url='https://github.com/nathforge/pydir',
    description='Pydir is mkdir for Python modules',
    long_description=open('README.txt').read(),
    
    author='Nathan Reynolds',
    author_email='email@nreynolds.co.uk',
    
    packages=['pydir'],
    package_dir={'': PACKAGE_PATH},
    entry_points = {
        'console_scripts': [
            'pydir = pydir:main',
        ],
    },
)
