#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['pandas>=1', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Simon Moulds and Simon Mudd",
    author_email='simon.m.mudd@ed.ac.uk',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    description="A simple package from getting data from the national river flow archive.",
    entry_points={
        'console_scripts': [
            'nrfapy_get_ts=nrfapy.nrfapy_get_ts:main',
        ],    
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='nrfapy,national river flow archive,hydrology,rivers,discharge,floods',
    name='nrfapy',
    packages=find_packages(include=['nrfapy', 'nrfapy.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/simon-m-mudd/nrfapy',
    version='0.2',
    zip_safe=False,
)
