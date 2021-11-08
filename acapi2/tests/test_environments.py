#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test Acquia Environments"""

import requests_mock

from acapi2.tests import BaseTest


@requests_mock.Mocker()
class TestEnvironments(BaseTest):
    def test_backups(self, mocker):
        env_id = "1-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        db_name = "db_name"
        uri = (
            f"{self.endpoint}/environments/{env_id}/"
            f"databases/{db_name}/backups"
        )

        response = {
            "total": 2,
            "pagination": {"total": 2, "limit": 2, "offset": 0},
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "1-a47ac10b-58cc-4372-a567-0e02b2c3d470/"
                    "databases/db_name/backups"
                },
                "parent": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "1-a47ac10b-58cc-4372-a567-0e02b2c3d470/"
                    "databases/db_name"
                },
                "limit": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "1-a47ac10b-58cc-4372-a567-0e02b2c3d470/databases"
                    "/db_name/backups{?limit}",
                    "templated": True,
                },
                "offset": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "1-a47ac10b-58cc-4372-a567-0e02b2c3d470/databases/"
                    "db_name/backups{?offset}",
                    "templated": True,
                },
                "sort": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "1-a47ac10b-58cc-4372-a567-0e02b2c3d470/"
                    "databases/db_name/backups{?sort}",
                    "templated": True,
                },
                "filter": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "1-a47ac10b-58cc-4372-a567-0e02b2c3d470/d"
                    "atabases/db_name/backups{?filter}",
                    "templated": True,
                },
            },
            "_embedded": {
                "items": [
                    {
                        "id": 1,
                        "database": {"id": 14, "name": "db_name"},
                        "type": "daily",
                        "started_at": "2012-05-15T12:00:00Z",
                        "completed_at": "2012-05-15T12:00:00Z",
                        "flags": {"deleted": False},
                        "environment": {
                            "id": "1-a47ac10b-58cc-4372-a567-0e02b2c3d470",
                            "name": "Production",
                        },
                        "_links": {
                            "self": {
                                "href": "https://cloud.acquia.com/api/"
                                "environments/1-a47ac10b-58cc-4372-"
                                "a567-0e02b2c3d470/databases/"
                                "db_name/backups/1"
                            },
                            "parent": {
                                "href": "https://cloud.acquia.com/api/"
                                "environments/1-a47ac10b-58cc-"
                                "4372-a567-0e02b2c3d470/databases"
                            },
                            "download": {
                                "href": "https://cloud.acquia.com/api/"
                                "environments/1-a47ac10b-58cc-4372"
                                "-a567-0e02b2c3d470/databases/"
                                "db_name/backups/1/actions/download"
                            },
                        },
                    },
                    {
                        "id": 2,
                        "database": {"id": 14, "name": "db_name"},
                        "type": "daily",
                        "started_at": "2012-03-28T12:00:00Z",
                        "completed_at": "2012-03-28T12:00:01Z",
                        "flags": {"deleted": False},
                        "environment": {
                            "id": "1-a47ac10b-58cc-4372-a567-0e02b2c3d470",
                            "name": "Production",
                        },
                        "_links": {
                            "self": {
                                "href": "https://cloud.acquia.com/api/"
                                "environments/1-a47ac10b-58cc-4372-"
                                "a567-0e02b2c3d470/databases/"
                                "db_name/backups/2"
                            },
                            "parent": {
                                "href": "https://cloud.acquia.com/api/"
                                "environments/1-a47ac10b-58cc-4372-"
                                "a567-0e02b2c3d470/databases"
                            },
                            "download": {
                                "href": "https://cloud.acquia.com/api/"
                                "environments/1-a47ac10b-58cc-4372-"
                                "a567-0e02b2c3d470/databases/db_name"
                                "/backups/2/actions/download"
                            },
                        },
                    },
                    {
                        "id": 3,
                        "database": {"id": 14, "name": "db_name"},
                        "type": "daily",
                        "started_at": "2017-01-08T04:00:00Z",
                        "completed_at": "2017-01-08T04:00:01Z",
                        "flags": {"deleted": False},
                        "environment": {
                            "id": "1-a47ac10b-58cc-4372-a567-0e02b2c3d470",
                            "name": "Production",
                        },
                        "_links": {
                            "self": {
                                "href": "https://cloud.acquia.com/api/"
                                "environments/1-a47ac10b-58cc-4372-"
                                "a567-0e02b2c3d470/databases/db_name"
                                "/backups/3"
                            },
                            "parent": {
                                "href": "https://cloud.acquia.com/api/"
                                "environments/1-a47ac10b-58cc-4372-"
                                "a567-0e02b2c3d470/databases"
                            },
                            "download": {
                                "href": "https://cloud.acquia.com/api/"
                                "environments/1-a47ac10b-58cc-4372-"
                                "a567-0e02b2c3d470/databases/db_name"
                                "/backups/3/actions/download"
                            },
                        },
                    },
                    {
                        "id": 4,
                        "database": {"id": 14, "name": "db_name"},
                        "type": "daily",
                        "started_at": "2017-01-08T05:00:02Z",
                        "completed_at": "2017-01-08T05:00:03Z",
                        "flags": {"deleted": False},
                        "environment": {
                            "id": "1-a47ac10b-58cc-4372-a567-0e02b2c3d470",
                            "name": "Production",
                        },
                        "_links": {
                            "self": {
                                "href": "https://cloud.acquia.com/api/"
                                "environments/1-a47ac10b-58cc-4372-"
                                "a567-0e02b2c3d470/databases/db_name"
                                "/backups/4"
                            },
                            "parent": {
                                "href": "https://cloud.acquia.com/api/"
                                "environments/1-a47ac10b-58cc-4372-"
                                "a567-0e02b2c3d470/databases"
                            },
                            "download": {
                                "href": "https://cloud.acquia.com/api/"
                                "environments/1-a47ac10b-58cc-4372-"
                                "a567-0e02b2c3d470/databases/db_name"
                                "/backups/4/actions/download"
                            },
                        },
                    },
                ]
            },
        }

        mocker.register_uri("GET", uri, status_code=200, json=response)

        response = self.acquia.environment(env_id).backups(db_name)
        self.assertEqual(response["total"], 2)
        self.assertIn("_embedded", response)

    def test_backup_details(self, mocker):
        env_id = "1-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        db_name = "db_name"
        id_backup = "1"
        uri = (
            f"{self.endpoint}/environments/{env_id}/"
            f"databases/{db_name}/backups/{id_backup}"
        )

        response = {
            "id": 1,
            "database": {"id": 14, "name": "db_name"},
            "type": "daily",
            "started_at": "2012-05-15T12:00:00Z",
            "completed_at": "2012-05-15T12:00:00Z",
            "flags": {"deleted": False},
            "environment": {
                "id": "1-a47ac10b-58cc-4372-a567-0e02b2c3d470",
                "name": "Production",
            },
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "1-a47ac10b-58cc-4372-a567-0e02b2c3d470/"
                    "database-backups/1"
                },
                "download": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "1-a47ac10b-58cc-4372-a567-0e02b2c3d470/"
                    "database-backups/1/actions/download"
                },
                "parent": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "1-a47ac10b-58cc-4372-a567-0e02b2c3d470/d"
                    "atabase-backups"
                },
            },
            "_embedded": {
                "environment": {
                    "id": "1-a47ac10b-58cc-4372-a567-0e02b2c3d470",
                    "name": "Production",
                    "_links": {
                        "self": {
                            "href": "https://cloud.acquia.com/api/"
                            "environments/1-a47ac10b-58cc-4372-"
                            "a567-0e02b2c3d470"
                        }
                    },
                },
                "database": {
                    "id": 14,
                    "name": "db_name",
                    "_links": {
                        "self": {
                            "href": "https://cloud.acquia.com/api/"
                            "environments/1-a47ac10b-58cc-4372-a567-"
                            "0e02b2c3d470/databases/db_name"
                        }
                    },
                },
            },
        }
        mocker.register_uri("GET", uri, status_code=200, json=response)

        response = self.acquia.environment(env_id).backup_details(
            db_name, id_backup
        )
        self.assertEqual(response["id"], 1)
        self.assertIn("_embedded", response)

    def test_backup_download(self, mocker):
        env_id = "1-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        db_name = "db_name"
        id_backup = "1"
        uri = (
            f"{self.endpoint}/environments/{env_id}/"
            f"databases/{db_name}/backups/{id_backup}/actions/download"
        )

        response = {
            "url": "http://test-site.com/AH_DOWNLOAD?t=1&d=/mnt/files/site/"
            "backups/on-demand/backup.sql.gz&dev=hash",
            "expires_at": "2020-03-27T10:26:51+00:00",
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "1-a47ac10b-58cc-4372-a567-0e02b2c3d470/databases/"
                    "db_name/backups/1/actions/download"
                },
                "parent": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "1-a47ac10b-58cc-4372-a567-0e02b2c3d470/databases/"
                    "db_name/backups/1/actions"
                },
            },
        }
        mocker.register_uri("GET", uri, status_code=200, json=response)

        response = self.acquia.environment(env_id).backup_download(
            db_name, id_backup
        )
        self.assertIn("url", response)

    def test_code_switch(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/environments/{env_id}/code/actions/switch"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)

        mocker.register_uri(
            "POST",
            uri,
            status_code=202,
            json={"message": "The code is being switched."},
        )

        response = self.acquia.environment(env_id).code_switch(
            "my-feature-branch"
        )

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
            "varnish_over_ssl": False,
        }

        response_message = {
            "message": "The environment configuration is being updated."
        }

        mocker.register_uri("PUT", uri, status_code=202, json=response_message)

        response = self.acquia.environment(env_id).configure(data)

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"updated", response.content)

    def test_create_backup(self, mocker):
        env_id = "1-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        db_name = "db_name"
        uri = (
            f"{self.endpoint}/environments/{env_id}/"
            f"databases/{db_name}/backups"
        )

        response = {
            "message": "Creating the backup.",
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "12-d314739e-296f-11e9-b210-d663bd873d93/"
                    "databases/my_db/backups/"
                },
                "notification": {
                    "href": "https://cloud.acquia.com/api/notifications/"
                    "42b56cff-0b55-4bdf-a949-1fd0fca61c6c"
                },
                "parent": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "12-d314739e-296f-11e9-b210-d663bd873d93/"
                    "databases/my_db/"
                },
            },
        }

        mocker.register_uri("POST", uri, status_code=202, json=response)
        response = self.acquia.environment(env_id).create_backup(db_name)
        self.assertEqual(response["message"], "Creating the backup.")
        self.assertIn("_links", response)

    def test_create_domain(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/environments/{env_id}/domains"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)

        response_message = {
            "message": "The domain 'ceruleanhq.com' is being added."
        }

        mocker.register_uri(
            "POST", uri, status_code=202, json=response_message
        )

        response = self.acquia.environment(env_id).create_domain(
            "ceruleanhq.com"
        )

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

        mocker.register_uri(
            "POST", uri, status_code=202, json=response_message
        )

        label = "Test destination"
        sources = ["apache-access", "apache-error"]
        consumer = "syslog"
        credentials = {
            "certificate": "-----BEGIN CERTIFICATE-----...\
            -----END CERTIFICATE-----"
        }
        address = "example.com:1234"

        response = self.acquia.environment(
            env_id
        ).create_log_forwarding_destinations(
            label, sources, consumer, credentials, address
        )

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"created", response.content)

    def test_delete_backup(self, mocker):
        env_id = "12-d314739e-296f-11e9-b210-d663bd873d93"
        db_name = "my_db"
        uri = (
            f"{self.endpoint}/environments/{env_id}/"
            f"databases/{db_name}/backups/1"
        )

        response = {
            "message": "Deleting the database backup.",
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/environments/12-d314"
                    "739e-296f-11e9-b210-d663bd873d93/databases/"
                    "my_db/backups/1"
                },
                "notification": {
                    "href": "https://cloud.acquia.com/api/notifications/42b5"
                    "6cff-0b55-4bdf-a949-1fd0fca61c6c"
                },
                "parent": {
                    "href": "https://cloud.acquia.com/api/environments/12-d31"
                    "4739e-296f-11e9-b210-d663bd873d93/databases/"
                    "my_db/backups"
                },
            },
        }

        mocker.register_uri("DELETE", uri, status_code=202, json=response)
        response = self.acquia.environment(env_id).delete_backup(db_name, 1)
        self.assertEqual(response["message"], "Deleting the database backup.")
        self.assertIn("_links", response)

    def test_delete_domain(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        domain = "ceruleanhq.com"
        uri = "{base_uri}/environments/{env_id}/domains/{domain}"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id, domain=domain)

        mocker.register_uri("DELETE", uri, status_code=202)

        response = self.acquia.environment(env_id).delete_domain(
            "ceruleanhq.com"
        )

        self.assertEqual(response.status_code, 202)

    def test_clear_varnish_domain(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        domain = "ceruleanhq.com"
        uri = (
            "{base_uri}/environments/{env_id}/domains/"
            "{domain}/actions/clear-varnish"
        )
        uri = uri.format(base_uri=self.endpoint, env_id=env_id, domain=domain)

        response_message = {
            "message": "Varnish is being cleared for domain 'ceruleanhq.com'."
        }

        mocker.register_uri(
            "POST", uri, status_code=202, json=response_message
        )

        response = self.acquia.environment(env_id).clear_varnish_domain(
            "ceruleanhq.com"
        )

        self.assertEqual(response.status_code, 202)

    def test_clear_varnish_domains(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        domains = ["ceruleanhq.com"]
        uri = (
            "{base_uri}/environments/{env_id}/domains/" "actions/clear-varnish"
        )
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)

        response_message = {
            "message": "Varnish is being cleared for the selected domains."
        }

        mocker.register_uri(
            "POST", uri, status_code=202, json=response_message
        )

        response = self.acquia.environment(env_id).clear_varnish_domains(
            domains
        )

        self.assertEqual(response.status_code, 202)

    def test_delete_log_forwarding_destinations(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        destination_uuid = "df4c5428-8d2e-453d-9edf-e412647449b1"
        uri = (
            f"{self.endpoint}/environments/{env_id}/"
            f"log-forwarding-destinations/{destination_uuid}"
        )

        response_message = {
            "message": "Log forwarding destination has been deleted."
        }

        mocker.register_uri(
            "DELETE", uri, status_code=202, json=response_message
        )

        response = self.acquia.environment(
            env_id
        ).delete_log_forwarding_destinations(destination_uuid)

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"deleted", response.content)

    def test_destroy(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/environments/{env_id}"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)
        response = {"message": "The environment is being deleted."}

        mocker.register_uri(
            url=uri, method="DELETE", status_code=202, json=response
        )

        response = self.acquia.environment(env_id).destroy()

        self.assertEqual(response.status_code, 202)

    def test_deploy_code(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        env_id_from = "14-0c7e79ab-1c4a-424e-8446-76ae8be7e851"
        uri = "{base_uri}/environments/{env_id}/code"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)

        response_message = {"message": "The code is being deployed."}

        mocker.register_uri(
            "POST", uri, status_code=202, json=response_message
        )

        response = self.acquia.environment(env_id).deploy_code(env_id_from)

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"deployed", response.content)

    def test_deploy_database(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        env_id_from = "14-0c7e79ab-1c4a-424e-8446-76ae8be7e851"
        uri = "{base_uri}/environments/{env_id}/databases"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)

        response_message = {"message": "The database is queued for copying."}

        mocker.register_uri(
            "POST", uri, status_code=202, json=response_message
        )

        response = self.acquia.environment(env_id).deploy_database(
            env_id_from, "my_new_db"
        )

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

        mocker.register_uri(
            "POST", uri, status_code=202, json=response_message
        )

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
                            "name": "prod",
                        },
                        "flags": {
                            "enabled": True,
                            "on_any_web": True,
                            "system": True,
                        },
                        "hour": "8",
                        "id": "43595",
                        "label": None,
                        "minute": "0",
                        "month": "*",
                        "server": [],
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
                            "name": "prod",
                        },
                        "flags": {
                            "enabled": True,
                            "on_any_web": True,
                            "system": False,
                        },
                        "hour": "*",
                        "id": "56834",
                        "label": "Site Cron Every Hour",
                        "minute": "0",
                        "month": "*",
                        "server": [],
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
                },
            },
            "total": 2,
        }

        mocker.register_uri("GET", uri, status_code=200, json=response_message)

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
                },
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
                                "expires_at": "2018-07-16T16:15:33+00:00",
                            },
                            "key": None,
                            "token": "4ded264c8891c400df8fc8905f07beb5f",
                        },
                        "sources": ["apache-access", "apache-error"],
                        "status": "active",
                        "flags": {
                            "enabled": True,
                            "certificate_expiring": False,
                        },
                        "environment": {
                            "id": "123-ea9060c5-1ed8-46ec-87d5-2ce2a0861577",
                            "name": "Test",
                        },
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
                                "expires_at": "2018-07-16T16:15:33+00:00",
                            },
                            "key": "1d0789d519c0b943cf38f401d30ffbdcd2",
                            "token": "4ded264c8891c400df8fc8905f07beb5f",
                        },
                        "sources": ["drupal-request", "drupal-watchdog"],
                        "status": "active",
                        "flags": {
                            "enabled": False,
                            "certificate_expiring": True,
                        },
                        "environment": {
                            "id": "123-ea9060c5-1ed8-46ec-87d5-2ce2a0861577",
                            "name": "Test",
                        },
                    },
                ]
            },
        }

        mocker.register_uri("GET", uri, status_code=200, json=response_message)

        response = self.acquia.environment(
            env_id
        ).get_log_forwarding_destinations()

        self.assertEqual(response["total"], 2)
        self.assertIn("_embedded", response)

    def test_get_php_version(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/environments/{env_id}/"
        uri = uri.format(base_uri=self.endpoint, env_id=env_id)
        response_message = {"configuration": {"php": {"version": "7.2"}}}

        mocker.register_uri("GET", uri, status_code=200, json=response_message)

        response = self.acquia.environment(env_id).get_php_version()

        self.assertEqual(response["php_version"], "7.2")

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
                },
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
                        "roles": ["web", "db"],
                        "ami_type": "c1.medium",
                        "configuration": {
                            "memcache": 64,
                            "ecu": 5,
                            "memory": 1.7,
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
                            "self_service": False,
                        },
                        "environment": {
                            "id": "24-a47ac10b-58cc-4372-a567-0e02b2c3d470",
                            "name": "dev",
                        },
                        "_links": {
                            "self": {
                                "href": "{baseUri}/environments/"
                                "24-a47ac10b-58cc-4372-a567-"
                                "0e02b2c3d470/servers/6"
                            }
                        },
                    },
                    {
                        "id": "4",
                        "name": "bal-4",
                        "hostname": "bal-4.servers.acquia.com",
                        "ssh_user": None,
                        "ip": "10.0.0.2",
                        "status": "normal",
                        "region": "us-west-1",
                        "roles": ["bal"],
                        "ami_type": "m1.small",
                        "configuration": {
                            "memcache": None,
                            "ecu": 1,
                            "memory": 1.7,
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
                            "self_service": False,
                        },
                        "environment": {
                            "id": "24-a47ac10b-58cc-4372-a567-0e02b2c3d470",
                            "name": "dev",
                        },
                        "_links": {
                            "self": {
                                "href": "{baseUri}/environments/"
                                "24-a47ac10b-58cc-4372-a567-"
                                "0e02b2c3d470/servers/4"
                            }
                        },
                    },
                ]
            },
        }

        mocker.register_uri("GET", uri, status_code=200, json=response_message)

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

    def test_update_log_forwarding_destinations(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        destination_uuid = "df4c5428-8d2e-453d-9edf-e412647449b1"
        uri = (
            f"{self.endpoint}/environments/{env_id}/"
            f"log-forwarding-destinations/{destination_uuid}"
        )

        response_message = {
            "message": "Log forwarding destination has been updated."
        }

        mocker.register_uri("PUT", uri, status_code=202, json=response_message)

        label = "Test destination"
        sources = ["apache-access", "apache-error"]
        consumer = "syslog"
        credentials = {
            "certificate": "-----BEGIN CERTIFICATE-----...\
            -----END CERTIFICATE-----"
        }
        address = "example.com:1234"

        response = self.acquia.environment(
            env_id
        ).update_log_forwarding_destinations(
            label, sources, consumer, credentials, address, destination_uuid
        )

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"updated", response.content)

    def test_enable_cron(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        cron_id = "1889"
        uri = (
            f"{self.endpoint}/environments/{env_id}/"
            f"crons/{cron_id}/actions/enable"
        )

        response = {
            "message": "The cron is being enabled.",
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "24-a47ac10b-58cc-4372-a567-0e02b2c3d470/crons/1889/"
                    "actions/enable"
                },
                "parent": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "24-a47ac10b-58cc-4372-a567-0e02b2c3d470/"
                    "crons/1889/actions"
                },
                "notification": {
                    "href": "https://cloud.acquia.com/api/notifications/"
                    "ceda2e82-54b7-4181-ae97-6a3163b187b8"
                },
            },
        }
        mocker.register_uri("POST", uri, status_code=202, json=response)

        response = self.acquia.environment(env_id).enable_cron(cron_id)

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"The cron is being enabled.", response.content)

    def test_disable_cron(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        cron_id = "1234"
        uri = (
            f"{self.endpoint}/environments/{env_id}/"
            f"crons/{cron_id}/actions/disable"
        )

        response = {
            "message": "The cron is being disabled.",
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "24-a47ac10b-58cc-4372-a567-0e02b2c3d470/crons/1234/"
                    "actions/disable"
                },
                "parent": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "24-a47ac10b-58cc-4372-a567-0e02b2c3d470/crons/"
                    "1234/actions"
                },
                "notification": {
                    "href": "https://cloud.acquia.com/api/notifications/"
                    "7b37b885-8ae4-454b-b8fa-ffaeff54f6a4"
                },
            },
        }
        mocker.register_uri("POST", uri, status_code=202, json=response)

        response = self.acquia.environment(env_id).disable_cron(cron_id)

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"The cron is being disabled.", response.content)

    def test_delete_cron(self, mocker):
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        cron_id = "1891"
        uri = f"{self.endpoint}/environments/{env_id}/" f"crons/{cron_id}"

        response = {
            "message": "Deleting cron.",
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "24-a47ac10b-58cc-4372-a567-0e02b2c3d470/crons/1891"
                },
                "parent": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "24-a47ac10b-58cc-4372-a567-0e02b2c3d470/crons"
                },
                "notification": {
                    "href": "https://cloud.acquia.com/api/notifications/"
                    "767cee8d-05f6-4761-a3dc-755957dfc9e6"
                },
            },
        }
        mocker.register_uri("DELETE", uri, status_code=202, json=response)

        response = self.acquia.environment(env_id).delete_cron(cron_id)

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"Deleting cron.", response.content)

    def test_get_ssl_settings(self, mocker):
        env_id = "3-110075c3-126e-6b43-c2ce-30be75fb33c2"
        uri = f"{self.endpoint}/environments/{env_id}/ssl"

        response = {
            "balancer": {"hostname": "example.us-east-1.elb.amazonaws.com"},
            "ips": ["127.0.0.1"],
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "3-110075c3-126e-6b43-c2ce-30be75fb33c2/ssl"
                },
                "certificates": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "3-110075c3-126e-6b43-c2ce-30be75fb33c2/ssl/certificates"
                },
                "csrs": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "3-110075c3-126e-6b43-c2ce-30be75fb33c2/ssl/csrs"
                },
                "parent": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "3-110075c3-126e-6b43-c2ce-30be75fb33c2"
                },
            },
        }

        mocker.register_uri("GET", uri, status_code=200, json=response)
        response = self.acquia.environment(env_id).get_ssl_settings()
        self.assertIn("balancer", response)

    def test_get_ssl_certs(self, mocker):
        env_id = "5-a1a10dab-62f4-418c-bc58-ab7742078ba8"
        uri = f"{self.endpoint}/environments/{env_id}/ssl/certificates"

        response = {
            "total": 3,
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "5-a1a10dab-62f4-418c-bc58-ab7742078ba8/ssl/certificates"
                },
                "parent": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "5-a1a10dab-62f4-418c-bc58-ab7742078ba8/ssl"
                },
            },
            "_embedded": {
                "items": [
                    {
                        "id": 7,
                        "label": None,
                        "certificate": "-----BEGIN CERTIFICATE-----...-----END CERTIFICATE-----",
                        "private_key": None,
                        "ca": "-----BEGIN CERTIFICATE-----...-----END CERTIFICATE-----",
                        "flags": {"active": True, "csr": True, "legacy": True},
                        "expires_at": "2022-03-28T00:12:34-0400",
                        "domains": ["example.com", "www.example.com"],
                        "environment": {
                            "id": "5-a1a10dab-62f4-418c-bc58-ab7742078ba8",
                            "name": "prod",
                        },
                        "_links": {
                            "self": {
                                "href": "https://cloud.acquia.com/api/environments/5-a1a10dab-62f4-418c-bc58-ab7742078ba8/ssl/certificates/7"
                            },
                            "csr": {
                                "href": "https://cloud.acquia.com/api/"
                                "environments/5-a1a10dab-62f4-418c-bc58-ab7742078ba8/ssl/csrs/7"
                            },
                        },
                    },
                    {
                        "id": 3,
                        "label": "Test Certificate 1",
                        "certificate": "-----BEGIN CERTIFICATE-----...-----END CERTIFICATE-----",
                        "private_key": "-----BEGIN RSA PRIVATE KEY-----...-----END RSA PRIVATE KEY-----",
                        "ca": "-----BEGIN CERTIFICATE-----...-----END CERTIFICATE-----",
                        "flags": {
                            "active": True,
                            "csr": False,
                            "legacy": False,
                        },
                        "expires_at": "2021-01-01T00:00:00-0400",
                        "domains": ["example2.com", "www.example2.com"],
                        "environment": {
                            "id": "5-a1a10dab-62f4-418c-bc58-ab7742078ba8",
                            "name": "prod",
                        },
                        "_links": {
                            "self": {
                                "href": "https://cloud.acquia.com/api/environments/5-a1a10dab-62f4-418c-bc58-ab7742078ba8/ssl/certificates/3"
                            }
                        },
                    },
                    {
                        "id": 4,
                        "label": "Test Certificate 2",
                        "certificate": "-----BEGIN CERTIFICATE-----...-----END CERTIFICATE-----",
                        "private_key": "-----BEGIN RSA PRIVATE KEY-----...-----END RSA PRIVATE KEY-----",
                        "ca": "-----BEGIN CERTIFICATE-----...-----END CERTIFICATE-----",
                        "flags": {
                            "active": False,
                            "csr": True,
                            "legacy": False,
                        },
                        "expires_at": "2021-01-01T00:00:00-0400",
                        "domains": ["example3.com", "www.example3.com"],
                        "environment": {
                            "id": "5-a1a10dab-62f4-418c-bc58-ab7742078ba8",
                            "name": "prod",
                        },
                        "_links": {
                            "self": {
                                "href": "https://cloud.acquia.com/api/environments/5-a1a10dab-62f4-418c-bc58-ab7742078ba8/ssl/certificates/4"
                            }
                        },
                    },
                ]
            },
        }

        mocker.register_uri("GET", uri, status_code=200, json=response)
        response = self.acquia.environment(env_id).get_ssl_certs()
        self.assertIn("certificate", response[0])

    def test_install_ssl_cert(self, mocker):
        env_id = "123-4ba86d4a-e193-4282-8963-d9d24746f444"
        uri = f"{self.endpoint}/environments/{env_id}/ssl/certificates"

        legacy = False
        certificate = (
            "-----BEGIN CERTIFICATE-----abc123....-----END CERTIFICATE-----",
        )
        private_key = (
            "-----BEGIN RSA PRIVATE KEY-----secret....-----END RSA PRIVATE KEY-----",
        )
        ca_certificates = (
            "-----BEGIN CERTIFICATE-----123abc....-----END CERTIFICATE-----",
        )
        csr_id = (123,)
        label = "My New Cert"

        response = {
            "message": "Installing the certificate.",
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/environments/123-4ba86d4a-e193-4282-8963-d9d24746f444/ssl/certificates"
                },
                "notification": {
                    "href": "https://cloud.acquia.com/api/notifications/8fdacf25-38e4-4621-b5de-e78638fe2ceb"
                },
                "parent": {
                    "href": "https://cloud.acquia.com/api/environments/123-4ba86d4a-e193-4282-8963-d9d24746f444/ssl"
                },
            },
        }

        mocker.register_uri("POST", uri, status_code=202, json=response)

        response = self.acquia.environment(env_id).install_ssl_cert(
            label, certificate, private_key, ca_certificates, legacy, csr_id
        )

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"Installing the certificate.", response.content)

    def test_get_ssl_cert(self, mocker):
        env_id = "5-9d46fd9d-e58b-47a3-8e9e-e8e0c2a854b4"
        cert_id = "13"
        uri = (
            f"{self.endpoint}/environments/{env_id}/ssl/certificates/{cert_id}"
        )

        response = {
            "id": 13,
            "label": "Test Certificate",
            "certificate": "-----BEGIN CERTIFICATE-----...-----END CERTIFICATE-----",
            "private_key": "-----BEGIN RSA PRIVATE KEY-----...-----END RSA PRIVATE KEY-----",
            "ca": "-----BEGIN CERTIFICATE-----...-----END CERTIFICATE-----",
            "flags": {"active": True, "csr": True, "legacy": False},
            "expires_at": "2022-03-28T00:12:34-0400",
            "domains": ["example.com", "www.example.com"],
            "environment": {
                "id": "5-9d46fd9d-e58b-47a3-8e9e-e8e0c2a854b4",
                "name": "prod",
            },
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "5-9d46fd9d-e58b-47a3-8e9e-e8e0c2a854b4/ssl/certificates/13"
                },
                "parent": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "5-9d46fd9d-e58b-47a3-8e9e-e8e0c2a854b4/ssl/certificates"
                },
            },
        }

        mocker.register_uri("GET", uri, status_code=200, json=response)
        response = self.acquia.environment(env_id).get_ssl_cert(cert_id)
        self.assertIn("certificate", response)

    def test_delete_ssl_cert(self, mocker):
        env_id = "286-a027502b-ad6c-a48e-a7e8-aa0def7d25e1"
        cert_id = "9"
        uri = (
            f"{self.endpoint}/environments/{env_id}/ssl/certificates/{cert_id}"
        )

        response = {
            "message": "Deleting the certificate.",
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/environments/286-a027502b-ad6c-a48e-a7e8-aa0def7d25e1/ssl/certificates/9"
                },
                "parent": {
                    "href": "https://cloud.acquia.com/api/environments/286-a027502b-ad6c-a48e-a7e8-aa0def7d25e1/ssl/certificates"
                },
                "notification": {
                    "href": "https://cloud.acquia.com/api/notifications/767cee8d-05f6-4761-a3dc-755957dfc9e6"
                },
            },
        }

        mocker.register_uri("DELETE", uri, status_code=202, json=response)
        response = self.acquia.environment(env_id).delete_ssl_cert(cert_id)
        self.assertEqual(response.status_code, 202)
        self.assertIn(b"Deleting the certificate.", response.content)

    def test_activate_ssl_cert(self, mocker):
        env_id = "123-a027502b-ad6c-a48e-a7e8-aa0def7d25e1"
        cert_id = "1"
        uri = f"{self.endpoint}/environments/{env_id}/ssl/certificates/{cert_id}/actions/activate"

        response = {
            "message": "Activating the certificate.",
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "123-a027502b-ad6c-a48e-a7e8-aa0def7d25e1/ssl/certificates/"
                    "1/actions/activate"
                },
                "notification": {
                    "href": "https://cloud.acquia.com/api/notifications/"
                    "4ee513c7-13b4-459f-af60-ba50c4f7cb5d"
                },
            },
        }

        mocker.register_uri("POST", uri, status_code=202, json=response)
        response = self.acquia.environment(env_id).activate_ssl_cert(cert_id)
        self.assertEqual(response.status_code, 202)
        self.assertIn(b"Activating the certificate.", response.content)

    def test_deactivate_ssl_cert(self, mocker):
        env_id = "123-a027502b-ad6c-a48e-a7e8-aa0def7d25e1"
        cert_id = "4547"
        uri = f"{self.endpoint}/environments/{env_id}/ssl/certificates/{cert_id}/actions/deactivate"

        response = {
            "message": "Deactivating the certificate.",
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/environments/"
                    "123-a027502b-ad6c-a48e-a7e8-aa0def7d25e1/ssl/certificates/"
                    "4547/actions/deactivate"
                },
                "notification": {
                    "href": "https://cloud.acquia.com/api/notifications/"
                    "cb5de18e-5721-4c26-9f67-1a7d806dd09e"
                },
            },
        }

        mocker.register_uri("POST", uri, status_code=202, json=response)
        response = self.acquia.environment(env_id).deactivate_ssl_cert(cert_id)
        self.assertEqual(response.status_code, 202)
        self.assertIn(b"Deactivating the certificate.", response.content)
