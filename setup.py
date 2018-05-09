#!/usr/bin/env python3
import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__name__), 'README.md')) as f:
    long_description = f.read()

setup(
    name='acapi2',
    version='2.0.0-a2',
    url='https://github.com/pmatias/python-acquia-cloud-2',
    download_url='https://pypi.org/project/acapi2',
    license='MIT',
    author='Pablo Fabregat',
    author_email='pablo@ceruleanhq.com',
    description='Acquia Cloud API v2 client library.',
    long_description=long_description,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
    ],
    platforms='any',
    python_requires='>=3.5',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=[
        'http-hmac-python==2.4.0',
        'requests==2.18.4',
        'requests-cache==0.4.13',
        'setuptools>=18.5'
    ]
)
