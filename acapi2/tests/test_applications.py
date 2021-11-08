#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Applications tests"""

import requests
import requests_mock

from acapi2.resources.applicationlist import ApplicationList
from acapi2.resources.environmentlist import EnvironmentList
from acapi2.tests import BaseTest


@requests_mock.Mocker()
class TestApplications(BaseTest):
    def test_application_list(self, mocker):
        response = {
            "total": 2,
            "pagination": {"total": 2, "limit": 10, "offset": 0},
            "_links": {
                "self": {"href": "{baseUri}/applications?limit=10"},
                "sort": {
                    "href": "{baseUri}/applications{?sort}",
                    "templated": True,
                },
                "filter": {
                    "href": "{baseUri}/applications{?filter}",
                    "templated": True,
                },
                "limit": {
                    "href": "{baseUri}/applications{?limit}",
                    "templated": True,
                },
                "parent": {"href": "{baseUri}"},
            },
            "_embedded": {
                "items": [
                    {
                        "id": 241643,
                        "uuid": "a47ac10b-58cc-4372" "-a567-0e02b2c3d470",
                        "name": "Sample application 1",
                        "hosting": {"type": "acp", "id": "devcloud:devcloud2"},
                        "subscription": {
                            "uuid": "s47ac10b-58cc-4372" "-a567-0e02b2c3d470",
                            "name": "Sample subscription",
                        },
                        "organization": {
                            "uuid": "g47ac10b-58cc-4372" "-a567-0e02b2c3d470",
                            "name": "Sample organization",
                        },
                        "flags": {
                            "remote_admin": True,
                            "service_management": True,
                        },
                        "type": "drupal",
                        "status": "normal",
                        "_links": {
                            "self": {
                                "href": "{baseUri}/applications/"
                                "a47ac10b-58cc-4372"
                                "-a567-0e02b2c3d470"
                            }
                        },
                    },
                    {
                        "id": 954291,
                        "uuid": "a47ac10b-58cc-4372" "-a567-0e02b2c3d471",
                        "name": "Sample application 2",
                        "hosting": {
                            "type": "free",
                            "id": "devcloud:devcloud2",
                        },
                        "subscription": {
                            "uuid": "s47ac10b-58cc-4372" "-a567-0e02b2c3d470",
                            "name": "Sample subscription",
                        },
                        "organization": {
                            "uuid": "g47ac10b-58cc-4372" "-a567-0e02b2c3d470",
                            "name": "Sample organization",
                        },
                        "type": "node",
                        "flags": {
                            "remote_admin": False,
                            "service_management": False,
                        },
                        "status": "provisioning",
                        "_links": {
                            "self": {
                                "href": "{baseUri}/applications/"
                                "a47ac10b-58cc-4372"
                                "-a567-0e02b2c3d471"
                            }
                        },
                    },
                ]
            },
        }

        uri = "{}/applications".format(self.endpoint)
        mocker.register_uri("GET", uri, json=response, status_code=200)

        apps = self.acquia.applications()
        self.assertIsInstance(apps, ApplicationList)

    def test_applications_filters(self, mocker):
        pass

    def test_application_not_found(self, mocker):
        app_uuid = "a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/applications/{uuid}"
        uri = uri.format(base_uri=self.endpoint, uuid=app_uuid)

        mocker.register_uri(url=uri, method="GET", status_code=404)

        acquia_data = self.acquia.application(app_uuid)

        with self.assertRaises(requests.HTTPError):
            acquia_data.request()

    def test_create_environment(self, mocker):
        response = {"message": "Adding an environment."}

        app_uuid = "a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/applications/{uuid}/environments"
        uri = uri.format(base_uri=self.endpoint, uuid=app_uuid)

        mocker.register_uri(
            url=uri, method="POST", status_code=202, json=response
        )

        response = self.acquia.application(app_uuid).create_environment(
            "Ticket Numer 123", "ticket-number-123", "ticket-number-123"
        )

        self.assertEqual(response.status_code, 202)

    def test_get_environments(self, mocker):
        response = {
            "total": 3,
            "_links": {
                "self": {
                    "href": "{baseUri}/applications/"
                    "a47ac10b-58cc-4372"
                    "-a567-0e02b2c3d470/environments"
                },
                "sort": {
                    "href": "{baseUri}/applications/"
                    "a47ac10b-58cc-4372"
                    "-a567-0e02b2c3d470/environments{?sort}",
                    "templated": True,
                },
                "filter": {
                    "href": "{baseUri}/applications/"
                    "a47ac10b-58cc-4372"
                    "-a567-0e02b2c3d470/"
                    "environments{?filter}",
                    "templated": True,
                },
                "limit": {
                    "href": "{baseUri}/applications/"
                    "a47ac10b-58cc-4372"
                    "-a567-0e02b2c3d470/environments{?limit}",
                    "templated": True,
                },
                "parent": {
                    "href": "{baseUri}/applications/"
                    "a47ac10b-58cc-4372-a567-0e02b2c3d470"
                },
            },
            "_embedded": {
                "items": [
                    {
                        "id": "24-a47ac10b-58cc-4372" "-a567-0e02b2c3d470",
                        "label": "Dev",
                        "name": "dev",
                        "application": {
                            "name": "Sample Drupal application",
                            "uuid": "a47ac10b-58cc-4372" "-a567-0e02b2c3d470",
                        },
                        "domains": [
                            "sitedev.hosted.acquia-sites.com",
                            "example.com",
                        ],
                        "active_domain": "example.com",
                        "default_domain": "sitedev.hosted" ".acquia-sites.com",
                        "image_url": None,
                        "ips": ["10.0.1.5"],
                        "region": "us-east-1",
                        "status": "normal",
                        "type": "drupal",
                        "size": None,
                        "weight": 0,
                        "vcs": {
                            "type": "git",
                            "path": "master",
                            "url": "site@svn-3.hosted."
                            "acquia-sites.com:site.git",
                        },
                        "insight": {
                            "status": "ok",
                            "scores": {"insight": 87, "seo": 56},
                            "counts": {
                                "best_practices": {
                                    "pass": 7,
                                    "fail": 0,
                                    "ignored": 0,
                                    "total": 7,
                                    "percent": 100,
                                },
                                "performance": {
                                    "pass": 22,
                                    "fail": 0,
                                    "ignored": 0,
                                    "total": 22,
                                    "percent": 100,
                                },
                                "security": {
                                    "pass": 23,
                                    "fail": 0,
                                    "ignored": 0,
                                    "total": 23,
                                    "percent": 100,
                                },
                            },
                        },
                        "flags": {
                            "cde": False,
                            "hsd": False,
                            "livedev": False,
                            "multi_region": False,
                            "production": False,
                            "production_mode": False,
                            "remote_admin": False,
                            "varnish": True,
                            "varnish_over_ssl": False,
                            "service_management": True,
                        },
                        "configuration": {
                            "operating_system": "precise",
                            "php": {
                                "version": "5.6",
                                "memory_limit": 128,
                                "apc": 96,
                                "max_execution_time": 300,
                                "max_post_size": 256,
                                "max_input_vars": 1000,
                                "sendmail_path": None,
                            },
                        },
                        "artifact": None,
                        "_links": {
                            "self": {
                                "href": "{baseUri}/environments/"
                                "24-a47ac10b-58cc-4372"
                                "-a567-0e02b2c3d470"
                            }
                        },
                    },
                    {
                        "id": "15-a47ac10b-58cc-4372" "-a567-0e02b2c3d470",
                        "label": "Production",
                        "name": "prod",
                        "application": {
                            "name": "Sample SiteFactory application",
                            "uuid": "a47ac10b-58cc-4372" "-a567-0e02b2c3d470",
                        },
                        "domains": [
                            "siteprod.hosted.acquia-sites.com",
                            "my-domain-prod.com",
                        ],
                        "gardener": {
                            "site-update": "my-domain-prod.com/admin/"
                            "gardens/site-update",
                            "multi-site": "my-domain-prod.com/"
                            "admin/gardens/staging",
                        },
                        "active_domain": "my-domain-prod.com",
                        "image_url": None,
                        "ips": ["10.0.1.1", "10.0.1.2"],
                        "region": "us-east-1",
                        "status": "normal",
                        "type": "drupal",
                        "size": None,
                        "weight": 0,
                        "vcs": {
                            "type": "git",
                            "path": "tags/01-01-2015",
                            "url": "site@svn-3.hosted."
                            "acquia-sites.com:site.git",
                        },
                        "insight": None,
                        "flags": {
                            "cde": False,
                            "hsd": False,
                            "livedev": False,
                            "multi_region": False,
                            "production": True,
                            "production_mode": True,
                            "remote_admin": False,
                            "varnish": True,
                            "varnish_over_ssl": False,
                            "service_management": False,
                        },
                        "configuration": None,
                        "artifact": None,
                        "_links": {
                            "self": {
                                "href": "{baseUri}/environments/"
                                "15-a47ac10b-58cc-4372"
                                "-a567-0e02b2c3d470"
                            }
                        },
                    },
                    {
                        "id": "32-a47ac10b-58cc-4372" "-a567-0e02b2c3d470",
                        "label": "Stage",
                        "name": "test",
                        "application": {
                            "name": "Sample Node application",
                            "uuid": "a47ac10b-58cc-4372" "-a567-0e02b2c3d470",
                        },
                        "domains": [
                            "sitetest.hosted.acquia-sites.com",
                            "my-domain-test.com",
                        ],
                        "active_domain": "my-domain-test.com",
                        "image_url": None,
                        "ips": [],
                        "region": "us-east-1",
                        "status": "normal",
                        "type": "node",
                        "size": "medium",
                        "weight": 20,
                        "vcs": {
                            "type": "git",
                            "path": None,
                            "url": "qa10@svn-3.networkdev."
                            "ahserversdev.com:qa10.git",
                        },
                        "insight": {
                            "status": "not-found",
                            "scores": None,
                            "counts": None,
                        },
                        "flags": {
                            "cde": False,
                            "hsd": False,
                            "livedev": False,
                            "multi_region": False,
                            "production": False,
                            "production_mode": False,
                            "remote_admin": False,
                            "varnish": True,
                            "varnish_over_ssl": False,
                            "service_management": False,
                        },
                        "configuration": {
                            "operating_system": "precise",
                            "node": {"version": "6.11.1"},
                        },
                        "artifact": {"id": 1, "name": "Example artifact"},
                        "_links": {
                            "self": {
                                "href": "{baseUri}/environments/"
                                "32-a47ac10b-58cc-4372"
                                "-a567-0e02b2c3d470"
                            }
                        },
                    },
                ]
            },
        }

        app_uuid = "a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/applications/{uuid}/environments".format(
            base_uri=self.endpoint, uuid=app_uuid
        )
        mocker.register_uri("GET", uri, json=response, status_code=200)

        envs = self.acquia.application(app_uuid).environments()
        self.assertIsInstance(envs, EnvironmentList)

    def test_application_permission(self, mocker):
        response = {
            "total": 53,
            "flags": {"administrator": False},
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/applications/"
                    "a47ac10b-58cc-4372-a567-0e02b2c3d470/permissions"
                },
                "parent": {
                    "href": "https://cloud.acquia.com/api/applications/"
                    "a47ac10b-58cc-4372-a567-0e02b2c3d470"
                },
            },
            "_embedded": {
                "items": [
                    {
                        "name": "administer alerts",
                        "label": "Manage Insight alerts",
                        "description": "Grants the ability to ignore alerts "
                        "and change settings on a "
                        "Drupal website "
                        'using the "Fix it Now" feature.',
                        "group_label": "Insight",
                    },
                    {
                        "name": "revoke insight installs",
                        "title": "Revoke Insight sites",
                        "description": "Grants the ability to revoke sites so "
                        "they can no longer submit data.",
                        "group_label": "Insight",
                    },
                    {
                        "name": "deploy to non-prod",
                        "label": "Pull and deploy code, files, or databases "
                        "to non-production environments",
                        "description": "Grants the ability to enable or "
                        "disable live development "
                        "and non-production "
                        "work.",
                        "group_label": "Workflow",
                    },
                    {
                        "name": "deploy to prod",
                        "label": "Deploy code, files, or databases to "
                        "the production environment",
                        "description": None,
                        "group_label": "Workflow",
                    },
                    {
                        "name": "pull from prod",
                        "label": "Pull files or databases from the "
                        "production environment",
                        "description": None,
                        "group_label": "Workflow",
                    },
                    {
                        "name": "move file to non-prod",
                        "label": "Move files to non-production environments",
                        "description": None,
                        "group_label": "Workflow",
                    },
                    {
                        "name": "move file to prod",
                        "label": "Move files to the production environment",
                        "description": None,
                        "group_label": "Workflow",
                    },
                    {
                        "name": "move file from prod",
                        "label": "Move files from production environments",
                        "description": None,
                        "group_label": "Workflow",
                    },
                    {
                        "name": "move file from non-prod",
                        "label": "Move files from non-production environments",
                        "description": None,
                        "group_label": "Workflow",
                    },
                    {
                        "name": "clear varnish on non-prod",
                        "label": "Clear Varnish cache for "
                        "non-production environments",
                        "description": None,
                        "group_label": "Workflow",
                    },
                    {
                        "name": "clear varnish on prod",
                        "label": "Clear Varnish cache for "
                        "the production environment",
                        "description": None,
                        "group_label": "Workflow",
                    },
                    {
                        "name": "configure prod env",
                        "label": "Configure production environment",
                        "description": None,
                        "group_label": "Workflow",
                    },
                    {
                        "name": "configure non-prod env",
                        "label": "Configure non-production environments",
                        "description": None,
                        "group_label": "Workflow",
                    },
                    {
                        "name": "add an environment",
                        "label": "Add an environment",
                        "description": None,
                        "group_label": "Workflow",
                    },
                    {
                        "name": "delete an environment",
                        "label": "Delete an environment",
                        "description": None,
                        "group_label": "Workflow",
                    },
                    {
                        "name": "administer domain non-prod",
                        "label": "Add or remove domains for "
                        "non-production environments",
                        "description": None,
                        "group_label": "Domains",
                    },
                    {
                        "name": "administer domain prod",
                        "label": "Add or remove domains for the "
                        "production environment",
                        "description": None,
                        "group_label": "Domains",
                    },
                    {
                        "name": "administer ssl prod",
                        "label": "Add or remove SSL certificates for "
                        "the production environment",
                        "description": None,
                        "group_label": "Domains",
                    },
                    {
                        "name": "administer ssl non-prod",
                        "label": "Add or remove SSL certificates for "
                        "the non-production environments",
                        "description": None,
                        "group_label": "Domains",
                    },
                    {
                        "name": "reboot server",
                        "label": "Reboot server",
                        "description": None,
                        "group_label": "Server administration",
                    },
                    {
                        "name": "resize server",
                        "label": "Resize server",
                        "description": "Increasing the size of your "
                        "server costs money.",
                        "group_label": "Server administration",
                    },
                    {
                        "name": "suspend server",
                        "label": "Suspend server",
                        "description": None,
                        "group_label": "Server administration",
                    },
                    {
                        "name": "configure server",
                        "label": "Configure server",
                        "description": None,
                        "group_label": "Server administration",
                    },
                    {
                        "name": "download logs non-prod",
                        "label": "Download logs for non-production "
                        "environments",
                        "description": None,
                        "group_label": "Logs",
                    },
                    {
                        "name": "download logs prod",
                        "label": "Download logs for the production"
                        " environment",
                        "description": None,
                        "group_label": "Logs",
                    },
                    {
                        "name": "add database",
                        "label": "Add a database",
                        "description": None,
                        "group_label": "Databases",
                    },
                    {
                        "name": "remove database",
                        "label": "Remove a database",
                        "description": None,
                        "group_label": "Databases",
                    },
                    {
                        "name": "view database connection",
                        "label": "View database connection details"
                        " (username, password, or hostname)",
                        "description": None,
                        "group_label": "Databases",
                    },
                    {
                        "name": "download db backup non-prod",
                        "label": "Download database backups for "
                        "non-production environments",
                        "description": None,
                        "group_label": "Databases",
                    },
                    {
                        "name": "download db backup prod",
                        "label": "Download database backups for "
                        "the production environment",
                        "description": None,
                        "group_label": "Databases",
                    },
                    {
                        "name": "create db backup non-prod",
                        "label": "Create database backups for "
                        "non-production environments",
                        "description": None,
                        "group_label": "Databases",
                    },
                    {
                        "name": "create db backup prod",
                        "label": "Create database backups for the "
                        "production environment",
                        "description": None,
                        "group_label": "Databases",
                    },
                    {
                        "name": "restore db backup non-prod",
                        "label": "Restore database backups for "
                        "non-production environments",
                        "description": None,
                        "group_label": "Databases",
                    },
                    {
                        "name": "restore db backup prod",
                        "label": "Restore database backups for "
                        "the production environment",
                        "description": None,
                        "group_label": "Databases",
                    },
                    {
                        "name": "administer team",
                        "label": "Add or remove a user of a team",
                        "description": "Granting this permission "
                        "will give any user with this "
                        "role full permissions on this team.",
                        "group_label": "Administration",
                    },
                    {
                        "name": "access cloud api",
                        "label": "Access the Cloud API",
                        "description": "Grants the ability to use "
                        "the API and bypass all other "
                        "permissions via command line tools.",
                        "group_label": "Administration",
                    },
                    {
                        "name": "activate add on",
                        "label": "Activate an Acquia Subscription add-on",
                        "description": None,
                        "group_label": "Administration",
                    },
                    {
                        "name": "administer cron non-prod",
                        "label": "Modify cron tasks for "
                        "non-production environments",
                        "description": None,
                        "group_label": "Cron",
                    },
                    {
                        "name": "administer cron prod",
                        "label": "Modify cron tasks for the "
                        "production environment",
                        "description": None,
                        "group_label": "Cron",
                    },
                    {
                        "name": "search limit increase",
                        "label": "Increase the search index "
                        "limit for a subscription",
                        "description": None,
                        "group_label": "Search",
                    },
                    {
                        "name": "search schema edit",
                        "label": "Edit the search schema for a subscription",
                        "description": None,
                        "group_label": "Search",
                    },
                    {
                        "name": "create support ticket",
                        "label": "Create a support ticket",
                        "description": None,
                        "group_label": "Support",
                    },
                    {
                        "name": "edit any support ticket",
                        "label": "View and edit any support tickets "
                        "for a subscription",
                        "description": None,
                        "group_label": "Support",
                    },
                    {
                        "name": "administer ssh keys",
                        "label": "Manage SSH keys",
                        "description": "Grants the ability to use SSH "
                        "and bypass all other permissions "
                        "via command line tools.",
                        "group_label": "SSH keys",
                    },
                    {
                        "name": "view build plans",
                        "label": "View Build plans",
                        "description": None,
                        "group_label": "Build",
                    },
                    {
                        "name": "edit build plans",
                        "label": "Edit Build plans",
                        "description": None,
                        "group_label": "Build",
                    },
                    {
                        "name": "run build plans",
                        "label": "Run Build plans",
                        "description": None,
                        "group_label": "Build",
                    },
                    {
                        "name": "add ssh key to git",
                        "label": "Add SSH key to git repository",
                        "description": None,
                        "group_label": "SSH keys",
                    },
                    {
                        "name": "add ssh key to non-prod",
                        "label": "Add SSH key to non-production environments",
                        "description": None,
                        "group_label": "SSH keys",
                    },
                    {
                        "name": "add ssh key to prod",
                        "label": "Add SSH key to the production environment",
                        "description": None,
                        "group_label": "SSH keys",
                    },
                    {
                        "name": "view remote administration",
                        "label": "View Remote Administration",
                        "description": "This permission is only relevant if "
                        "your subscription has remote "
                        "administration.",
                        "group_label": "Administration",
                    },
                    {
                        "name": "edit remote administration",
                        "label": "Edit Remote Administration",
                        "description": "This permission is only relevant "
                        "if your subscription has remote "
                        "administration.",
                        "group_label": "Administration",
                    },
                ]
            },
        }

        app_uuid = "a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = f"{self.endpoint}/applications/{app_uuid}/permissions"
        mocker.register_uri("GET", uri, json=response, status_code=200)

        perms = self.acquia.application(app_uuid).permissions()

        self.assertEqual(perms.status_code, 200)
        self.assertIn(b"remote", perms.content)
