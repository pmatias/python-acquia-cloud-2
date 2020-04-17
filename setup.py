#!/usr/bin/env python3
import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__name__), 'README.md')) as f:
    long_description = f.read()

setup(
    name='acapi2',
    version='2.0.4',
    url='https://github.com/pmatias/python-acquia-cloud-2',
    download_url='https://pypi.org/project/acapi2',
    license='MIT',
    author='Pablo Fabregat',
    author_email='pablo@ceruleanhq.com',
    description='Acquia Cloud API v2 client library.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
    ],
    platforms='any',
    python_requires='>=3.6',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=[
        'backoff==1.10.0',
        'http-hmac-python>=2.4.0',
        'requests>=2.20.0',
        'requests-cache>=0.5.2',
        'setuptools>=38.5'
    ]
)
