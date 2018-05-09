#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='acapi2',
    version='2.0.0-alpha1',
    url='https://github.com/pmatias/python-acquia-cloud-2',
    download_url='https://pypi.python.org/pypi/TBD',
    license='MIT',
    author='Pablo Fabregat',
    author_email='pablo@ceruleanhq.com',
    description='Acquia Cloud API v2 client.',
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
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=[
        'http-hmac-python==2.4.0',
        'requests==2.18.4',
        'requests-cache==0.4.13',
        'setuptools>=18.5'
    ]
)
