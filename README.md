# Python Acquia Cloud API v2

Python Client library to communicate with the [Acquia Cloud API V2](http://cloud.acquia.com/api-docs).

[Pablo Fabregat](http://pablofabregat.com) - [License](LICENSE.txt)

[![Build Status](https://travis-ci.org/pmatias/python-acquia-cloud-2.svg?branch=master)](https://travis-ci.org/pmatias/python-acquia-cloud-2) [![Documentation Status](https://readthedocs.org/projects/acapi2/badge/?version=latest)](https://acapi2.readthedocs.io/en/latest/?badge=latest) [![codecov](https://codecov.io/gh/pmatias/python-acquia-cloud-2/branch/2.x/graph/badge.svg)](https://codecov.io/gh/pmatias/python-acquia-cloud-2)


## Deprecation notice:

The following items will be removed in 2.0.3:

* Support for environment variables `ACQUIA_CLOUD_API_KEY` and 
`ACQUIA_CLOUD_API_SECRET`; how the credentials are provided to the library is
responsibility of the user.
* Tasks object; Acquia API is deprecating this as well, the Notifications object
should be used instead   

## Examples

Please bear in mind that the library is being actively developed and
most of its functionality is just a reduced set of what it should be.

Minimal request

```python
acquia = Acquia(api_key, api_secret)
application = acquia.application("a47ac10b-58cc-4372-a567-0e02b2c3d470")

print(application["name"])
```

### Using filters

```python
subscription_name = "MySubsName"
filters = "name=" + subscription_name

application = acapi.applications(filters=filters).first()
dev_environment = application.environments()["dev"]

print(dev_environment["id"])

dev_environment.set_php_version("7.0")

more_settings = {
  "max_execution_time": 10,
  "memory_limit": 192,
  "apc": 128,
  "max_input_vars": 1000,
  "max_post_size": 256,
  "sendmail_path": "/usr/bin/sendmail",
  "varnish_over_ssl": False
}

dev_environment.configure(more_settings)
```

### Notifications

acapi2 now supports [the notifications endpoint](https://cloudapi-docs.acquia.com/#/Notifications/getNotificationByUuid)

Whenever an action is executed (e.g. [a code import](https://cloudapi-docs.acquia.com/#/Environments/postEnvironmentsImportSite)),
 the API will return a uuid for its correspondant 
task status (notification), this can be used to check on the status of the task itself"

```python
notif_uuid = "d82a122d-b7b8-46fc-9999-39cb824fac8d"
notification = acquia.notification(notif_uuid)
print(notification.data)
```

You can also check on the [current notifications for a specific application](https://cloudapi-docs.acquia.com/#/Applications/getApplicationNotifications)

````python
filters = "name=@*myapp*"
app = acquia.applications(filters=filters).first()

notifications = app.notifications()
for uuid, notification in notifications.items():
        print(notification.data)
````

## Roadmap

Current version: **2.0.3**

### 2.0.1

* 2.x becomes the default repository branch,
* Out of the beta status,
* Notifications support,
* Code coverage increase,
* Clean up the original code a bit.
* Support for backups.

### 2.0.2

* Small release to put back support of credentials in environment variables,
which is now being announced as deprecated.

### 2.0.3

* Tasks endpoint removal (you should use notifications),
* Credential environment variables removal,
* Wait until a notification completes,
* More support for log forwarding

### 2.0.4

* Minor release: Added support for DB Backup Downloads

### 2.0.5
* Credential environment variables removal (now for real :) ),
* Distributions endpoint support,
* Messages endpoint support,
* Better exceptions handling.

## Credits

This library was originally based on the Acquia API Python Library created 
by Dave Hall (http://github.com/skwashd/python-acquia-cloud)
