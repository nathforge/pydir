#!/usr/bin/env python

from setuptools import setup

setup(
    name='pydir',
    version='1.01',
    description='Pydir is mkdir for Python modules',
    long_description=open('README.txt').read(),
    author='Nathan Reynolds',
    url='https://github.com/nathforge/pydir',
    zip_safe=True,
    entry_points = {
        'console_scripts': [
            'pydir=pydir:main',
        ],
    },
)

