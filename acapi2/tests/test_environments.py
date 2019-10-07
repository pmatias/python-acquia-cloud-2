#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test Acquia Environments"""

import requests_mock

from acapi2.tests import BaseTest


@requests_mock.Mocker()
class TestEnvironments(BaseTest):

    def test_code_switch(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/environments/{env_id}/code/actions/switch"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)

        mocker.register_uri("POST", uri, status_code=202,
                            json={"message": "The code is being switched."})

        response = self.acquia.environment(env_id).code_switch(
            "my-feature-branch")

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"switched", response.content)

    def test_configure(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/environments/{env_id}"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)

        data = {
            "version": "5.5",
            "max_execution_time": 10,
            "memory_limit": 192,
            "apc": 128,
            "max_input_vars": 1000,
            "max_post_size": 256,
            "sendmail_path": "/usr/bin/sendmail",
            "varnish_over_ssl": False
        }

        response_message = {
            "message": "The environment configuration is being updated."
        }

        mocker.register_uri("PUT", uri, status_code=202, json=response_message)

        response = self.acquia.environment(env_id).configure(data)

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"updated", response.content)

    def test_create_domain(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/environments/{env_id}/domains"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)

        response_message = {
            "message": "The domain 'ceruleanhq.com' is being added."
        }

        mocker.register_uri("POST", uri,
                            status_code=202, json=response_message)

        response = self.acquia.environment(env_id).create_domain(
            "ceruleanhq.com")

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"added", response.content)

    def test_create_log_forwarding_destinations(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/environments/{env_id}/log-forwarding-destinations"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)

        response_message = {
            "message": "Log forwarding destination for the \
            environment has been created."
        }

        mocker.register_uri("POST", uri,
                            status_code=202, json=response_message)

        label = "Test destination"
        sources = [
            "apache-access",
            "apache-error"
        ]
        consumer = "syslog"
        credentials = {
            "certificate": "-----BEGIN CERTIFICATE-----...\
            -----END CERTIFICATE-----"
        }
        address = "example.com:1234"

        response = self.acquia.environment(
                   env_id).create_log_forwarding_destinations(
                   label, sources, consumer, credentials, address)

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"created", response.content)

    def test_delete_domain(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        domain = "ceruleanhq.com"
        uri = "{base_uri}/environments/{env_id}/domains/{domain}"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id, domain=domain)

        mocker.register_uri("DELETE", uri,
                            status_code=202)

        response = self.acquia.environment(env_id).delete_domain(
            "ceruleanhq.com")

        self.assertEqual(response.status_code, 202)

    def test_clear_varnish_domain(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        domain = "ceruleanhq.com"
        uri = "{base_uri}/environments/{env_id}/domains/"\
              "{domain}/actions/clear-varnish"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id, domain=domain)

        response_message = {
            "message": "Varnish is being cleared for domain 'ceruleanhq.com'."
        }

        mocker.register_uri("POST", uri,
                            status_code=202, json=response_message)

        response = self.acquia.environment(
            env_id).clear_varnish_domain("ceruleanhq.com")

        self.assertEqual(response.status_code, 202)

    def test_destroy(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/environments/{env_id}"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)
        response = {
            "message": "The environment is being deleted."
        }

        mocker.register_uri(url=uri, method="DELETE",
                            status_code=202, json=response)

        response = self.acquia.environment(env_id).destroy()

        self.assertEqual(response.status_code, 202)

    def test_deploy_code(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        env_id_from = "14-0c7e79ab-1c4a-424e-8446-76ae8be7e851"
        uri = "{base_uri}/environments/{env_id}/code"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)

        response_message = {
            "message": "The code is being deployed."
        }

        mocker.register_uri("POST", uri,
                            status_code=202, json=response_message)

        response = self.acquia.environment(env_id).deploy_code(env_id_from)

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"deployed", response.content)

    def test_deploy_database(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        env_id_from = "14-0c7e79ab-1c4a-424e-8446-76ae8be7e851"
        uri = "{base_uri}/environments/{env_id}/databases"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)

        response_message = {
            "message": "The database is queued for copying."
        }

        mocker.register_uri("POST", uri,
                            status_code=202, json=response_message)

        response = self.acquia.environment(env_id).deploy_database(
            env_id_from, "my_new_db")

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"queued", response.content)

    def test_deploy_files(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        env_id_from = "14-0c7e79ab-1c4a-424e-8446-76ae8be7e851"
        uri = "{base_uri}/environments/{env_id}/files"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)

        response_message = {
            "message": "The files have been queued for copying."
        }

        mocker.register_uri("POST", uri,
                            status_code=202, json=response_message)

        response = self.acquia.environment(env_id).deploy_files(env_id_from)

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"queued", response.content)

    def test_get_crons(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/environments/{env_id}/crons"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)
        response_message = {
            "_embedded": {
                "items": [
                    {
                        "_links": {
                            "self": {
                                "href": "{baseUri}/environments/24-a47ac10b-58cc-4372-a567-0e02b2c3d470\
                                /crons/43595"
                            }
                        },
                        "command": "/usr/local/bin/drush -r /var/www/html/mysub/docroot \
                                   ah-db-backup mysub",
                        "day_month": "*",
                        "day_week": "*",
                        "environment": {
                            "id": "24-a47ac10b-58cc-4372-a567-0e02b2c3d470",
                            "name": "prod"
                        },
                        "flags": {
                            "enabled": True,
                            "on_any_web": True,
                            "system": True
                        },
                        "hour": "8",
                        "id": "43595",
                        "label": None,
                        "minute": "0",
                        "month": "*",
                        "server": []
                    },
                    {
                        "_links": {
                            "self": {
                                "href": "{baseUri}/environments/24-a47ac10b-58cc-4372-a567-0e02b2c3d470\
                                /crons/56834"
                            }
                        },
                        "command": "/usr/local/bin/drush9 --uri=[http://[site-uri] \
                                --root=/var/www/html/${AH_SITE_NAME}/docroot \
                                -dv cron &>> /var/log/sites/${AH_SITE_NAME}\
                                /logs/$(hostname -s)/drush-cron.log",
                        "day_month": "*",
                        "day_week": "*",
                        "environment": {
                            "id": "24-a47ac10b-58cc-4372-a567-0e02b2c3d470",
                            "name": "prod"
                        },
                        "flags": {
                            "enabled": True,
                            "on_any_web": True,
                            "system": False
                        },
                        "hour": "*",
                        "id": "56834",
                        "label": "Site Cron Every Hour",
                        "minute": "0",
                        "month": "*",
                        "server": []
                    },
                ]
            },
            "_links": {
                "parent": {
                    "href": "{baseUri}/environments/\
                            24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
                },
                "self": {
                    "href": "{baseUri}/environments/\
                            24-a47ac10b-58cc-4372-a567-0e02b2c3d470/crons"
                }
            },
            "total": 2
        }

        mocker.register_uri("GET", uri,
                            status_code=200, json=response_message)

        response = self.acquia.environment(env_id).get_crons()

        self.assertEqual(response["total"], 2)
        self.assertIn("_embedded", response)

    def test_get_log_forwarding_destinations(self, mocker):
        env_id = "5-185f07c7-9c4f-407b-8968-67892ebcb38a"
        uri = "{base_uri}/environments/{env_id}/log-forwarding-destinations"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)
        response_message = {
            "total": 2,
            "_links": {
                "self": {
                    "href": "{base_uri}/environments/5-185f07c7-9c4f-407b-8968-67892ebcb38a\
                    /log-forwarding-destinations"
                },
                "parent": {
                    "href": "{base_uri}/environments\
                    /5-185f07c7-9c4f-407b-8968-67892ebcb38a"
                }
            },
            "_embedded": {
                "items": [
                    {
                        "uuid": "df4c5428-8d2e-453d-9edf-e412647449b1",
                        "label": "Test destination",
                        "consumer": "sumologic",
                        "address": "example.com:1234",
                        "credentials": {
                            "certificate": {
                                "certificate": "-----BEGIN CERTIFICATE-----...\
                                -----END CERTIFICATE-----",
                                "expires_at": "2018-07-16T16:15:33+00:00"
                            },
                            "key": None,
                            "token": "4ded264c8891c400df8fc8905f07beb5f"
                        },
                        "sources": [
                            "apache-access",
                            "apache-error"
                        ],
                        "status": "active",
                        "flags": {
                            "enabled": True,
                            "certificate_expiring": False
                        },
                        "environment": {
                            "id": "123-ea9060c5-1ed8-46ec-87d5-2ce2a0861577",
                            "name": "Test"
                        }
                    },
                    {
                        "uuid": "df4c5428-8d2e-453d-9edf-e412647449b5",
                        "label": "Another test destination",
                        "consumer": "syslog",
                        "address": "193.169.2.19:5678",
                        "credentials": {
                            "certificate": {
                                "certificate": "-----BEGIN CERTIFICATE-----...\
                                -----END CERTIFICATE-----",
                                "expires_at": "2018-07-16T16:15:33+00:00"
                            },
                            "key": "1d0789d519c0b943cf38f401d30ffbdcd2",
                            "token": "4ded264c8891c400df8fc8905f07beb5f"
                        },
                        "sources": [
                            "drupal-request",
                            "drupal-watchdog"
                        ],
                        "status": "active",
                        "flags": {
                            "enabled": False,
                            "certificate_expiring": True
                        },
                        "environment": {
                            "id": "123-ea9060c5-1ed8-46ec-87d5-2ce2a0861577",
                            "name": "Test"
                        }
                    }
                ]
            }
        }

        mocker.register_uri("GET", uri,
                            status_code=200, json=response_message)

        response = self.acquia.environment(
            env_id).get_log_forwarding_destinations()

        self.assertEqual(response["total"], 2)
        self.assertIn("_embedded", response)

    def test_get_php_version(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/environments/{env_id}/"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)
        response_message = {
            'configuration': {
                'php': {
                    'version': '7.2'
                }
            }
        }

        mocker.register_uri("GET", uri,
                            status_code=200, json=response_message)

        response = self.acquia.environment(env_id).get_php_version()

        self.assertEqual(response['php_version'], '7.2')

    def test_get_servers(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/environments/{env_id}/servers"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)

        response_message = {
            "total": 2,
            "_links": {
                "self": {
                    "href": "{baseUri}/environments/"
                            "24-a47ac10b-58cc-4372-a567-0e02b2c3d470/servers"
                },
                "parent": {
                    "href": "{baseUri}/environments/"
                            "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
                }
            },
            "_embedded": {
                "items": [
                    {
                        "id": "6",
                        "name": "ded-6",
                        "hostname": "ded-6.servers.acquia.com",
                        "ssh_user": "user.dev",
                        "ip": "10.0.0.1",
                        "status": "normal",
                        "region": "us-west-1",
                        "roles": [
                            "web",
                            "db"
                        ],
                        "ami_type": "c1.medium",
                        "configuration": {
                            "memcache": 64,
                            "ecu": 5,
                            "memory": 1.7
                        },
                        "flags": {
                            "elastic_ip": False,
                            "active_web": True,
                            "active_bal": False,
                            "primary_db": True,
                            "web": True,
                            "database": True,
                            "balancer": False,
                            "memcache": True,
                            "dedicated": False,
                            "self_service": False
                        },
                        "environment": {
                            "id": "24-a47ac10b-58cc-4372-a567-0e02b2c3d470",
                            "name": "dev"
                        },
                        "_links": {
                            "self": {
                                "href": "{baseUri}/environments/"
                                        "24-a47ac10b-58cc-4372-a567-"
                                        "0e02b2c3d470/servers/6"
                            }
                        }
                    },
                    {
                        "id": "4",
                        "name": "bal-4",
                        "hostname": "bal-4.servers.acquia.com",
                        "ssh_user": None,
                        "ip": "10.0.0.2",
                        "status": "normal",
                        "region": "us-west-1",
                        "roles": [
                            "bal"
                        ],
                        "ami_type": "m1.small",
                        "configuration": {
                            "memcache": None,
                            "ecu": 1,
                            "memory": 1.7
                        },
                        "flags": {
                            "elastic_ip": False,
                            "active_web": False,
                            "active_bal": False,
                            "primary_db": True,
                            "web": False,
                            "database": False,
                            "balancer": True,
                            "memcache": False,
                            "dedicated": True,
                            "self_service": False
                        },
                        "environment": {
                            "id": "24-a47ac10b-58cc-4372-a567-0e02b2c3d470",
                            "name": "dev"
                        },
                        "_links": {
                            "self": {
                                "href": "{baseUri}/environments/"
                                        "24-a47ac10b-58cc-4372-a567-"
                                        "0e02b2c3d470/servers/4"
                            }
                        }
                    }
                ]
            }
        }

        mocker.register_uri("GET", uri,
                            status_code=200, json=response_message)

        response = self.acquia.environment(env_id).get_servers()

        self.assertEqual(response["total"], 2)
        self.assertIn("_embedded", response)

    def test_set_php_version(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/environments/{env_id}"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)

        response_message = {
            "message": "The environment configuration is being updated."
        }

        mocker.register_uri("PUT", uri, status_code=202, json=response_message)

        response = self.acquia.environment(env_id).set_php_version("7.0")

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"updated", response.content)
