#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='NimingCypher',
    version="2.6.0",
    description='Encryption module for instant messaging',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Arnaud Gissinger',
    license='CC ANCSA 4.0',
    classifiers=[
        #https://pypi.python.org/pypi?%3Aaction=list_classifiers
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Topic :: Security :: Cryptography',

        # Pick your license as you wish (should match "license" above)
        'License :: Free for non-commercial use',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        ],
    keywords='encryption module instant messaging free',
    install_requires=['beautifulsoup4','rsa'],
    packages=find_packages(),
)
