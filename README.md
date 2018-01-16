# Python Acquia Cloud API v2

[![Build Status](https://travis-ci.org/pmatias/python-acquia-cloud-2.svg?branch=master)](https://travis-ci.org/pmatias/python-acquia-cloud-2) [![codecov](https://codecov.io/gh/pmatias/python-acquia-cloud-2/branch/master/graph/badge.svg)](https://codecov.io/gh/pmatias/python-acquia-cloud-2)
 [![Say Thanks](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/pmatias)

Python implementation for the new Acquia API v2 (https://cloud.acquia.com/api-docs/),
based on the original acapi Python Library created by Dave Hall (http://github.com/skwashd/python-acquia-cloud)


This library is a WIP and it is in an unusable state.

### Roadmap

* Testing testing testing,
* First alpha goal: get the lib to create environments on demand (Delayed because Acquia's API design),
* Submit to Pypi

More information coming soon.


## Examples

Please bear in mind that the library is being actively developed and
most of its functionality is just a reduced set of what it should be.

Minimal request

```
acquia = Acquia(api_key, api_secret)
application = acquia.application("a47ac10b-58cc-4372-a567-0e02b2c3d470")

print(application["name"])
```

### Using filters

```
subscription_name = "MySubsName"
filters = "name=" + subscription_name

application = acapi.applications(filters=filters).first()
dev_environment = application.environments()["dev"]

print(dev_environment["id"])

dev_environment.set_php_version("7.0")
```