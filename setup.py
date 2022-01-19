#!/usr/bin/env python3
import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__name__), "README.md")) as f:
    long_description = f.read()

setup(
    name="acapi2",
    version="2.1.2",
    url="https://github.com/pmatias/python-acquia-cloud-2",
    download_url="https://pypi.org/project/acapi2",
    license="MIT",
    author="Matt Katz",
    author_email="matt@ceruleanhq.nl",
    description="Acquia Cloud API v2 client library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet",
    ],
    platforms="any",
    python_requires=">=3.6",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "backoff>=1.10.0,<2",
        "http-hmac-python>=2.4.1,<3",
        "requests>=2.25.0,<=3.0",
        "requests-cache>=0.5.2,<0.9.2",
        "setuptools>=38.5",
    ],
)
