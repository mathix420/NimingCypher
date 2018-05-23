#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='NimingCypher',
    version="2.0.1",
    description='High security encryption module for instant messaging',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Arnaud Gissinger',
    license='MIT',
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
         'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        ],
    keywords='encryption module instant messaging free',
    install_requires=['beautifulsoup4'],
    packages=find_packages(),
)
