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
