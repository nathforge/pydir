#!/usr/bin/env python

from setuptools import setup

setup(
    name='pydir',
    version='0.1',
    description='Pydir is mkdir for Python modules',
    long_description=open('README.txt').read(),
    author='Nathan Reynolds',
    url='https://github.com/nathforge/pydir',
    zip_safe=True,
    packages=['pydir'],
    entry_points = {
        'console_scripts': [
            'pydir=pydir:main',
        ],
    },
)

