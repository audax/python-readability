#!/usr/bin/env python
from setuptools import setup, find_packages
import sys

if sys.version < '3':
    chardet_module = "chardet"
else:
    chardet_module = "chardet2"


setup(
    name="readability-lxml",
    version="0.2.6.1.1",
    author="Yuri Baburov",
    author_email="burchik@gmail.com",
    description="fast python port of arc90's readability tool",
    test_suite = "tests.test_article_only",
    long_description=open("README").read(),
    license="Apache License 2.0",
    url="https://github.com/audax/python-readability",
    packages=['readability'],
    install_requires=[
        chardet_module,
        "lxml"
        ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
)
