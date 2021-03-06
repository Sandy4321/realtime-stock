#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [

]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='realtime-stock',
    version='1.0.0',
    description="A python package to gather realtime stock quotes from " +
                "Yahoo Finance. The package enables you to handle single " +
                "stocks or portfolios, optimizing the nunber of requests " +
                "necessary to gather quotes for a large number of stocks.",
    long_description=readme + '\n\n' + history,
    author="Rafael Lopes Conde dos Reis",
    author_email='rafael.lcreis@gmail.com',
    url='https://github.com/condereis/realtime-stock',
    packages=[
        'rtstock',
    ],
    package_dir={'rtstock':
                 'rtstock'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='rtstock',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
