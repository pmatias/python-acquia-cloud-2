#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test Permissions Endpoint"""

import requests_mock

from acapi2.resources.permissionslist import PermissionsList
from acapi2.tests import BaseTest


@requests_mock.Mocker()
class TestPermissions(BaseTest):
    def test_permissions_list(self, mocker):
        response = {
            "total": 53,
            "_links": {
                "self": {"href": "https://cloud.acquia.com/api/permissions"}
            },
            "_embedded": {
                "items": [
                    {
                        "name": "administer alerts",
                        "label": "Manage Insight alerts",
                        "description": "Grants the ability to ignore alerts "
                        "and change settings on a "
                        "Drupal website "
                        "using the Fix it Now feature.",
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
                        "disable live development and "
                        "non-production "
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
                        "label": "Clear Varnish cache for the "
                        "production environment",
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
                        "label": "Add or remove SSL certificates "
                        "for the production environment",
                        "description": None,
                        "group_label": "Domains",
                    },
                    {
                        "name": "administer ssl non-prod",
                        "label": "Add or remove SSL certificates "
                        "for the non-production environments",
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
                        "label": "Download logs for the production "
                        "environment",
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
                        "label": "View database connection details "
                        "(username, password, or hostname)",
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
                        "label": "Download database backups for the "
                        "production environment",
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
                        "label": "Create database backups "
                        "for the production environment",
                        "description": None,
                        "group_label": "Databases",
                    },
                    {
                        "name": "restore db backup non-prod",
                        "label": "Restore database backups "
                        "for non-production environments",
                        "description": None,
                        "group_label": "Databases",
                    },
                    {
                        "name": "restore db backup prod",
                        "label": "Restore database backups "
                        "for the production environment",
                        "description": None,
                        "group_label": "Databases",
                    },
                    {
                        "name": "administer team",
                        "label": "Add or remove a user of a team",
                        "description": "Granting this permission will "
                        "give any user with this "
                        "role full permissions "
                        "on this team.",
                        "group_label": "Administration",
                    },
                    {
                        "name": "access cloud api",
                        "label": "Access the Cloud API",
                        "description": "Grants the ability to use the"
                        " API and bypass all other permissions "
                        "via command line tools.",
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
                        "label": "Modify cron tasks for non-production "
                        "environments",
                        "description": None,
                        "group_label": "Cron",
                    },
                    {
                        "name": "administer cron prod",
                        "label": "Modify cron tasks for the production "
                        "environment",
                        "description": None,
                        "group_label": "Cron",
                    },
                    {
                        "name": "search limit increase",
                        "label": "Increase the search index limit for a "
                        "subscription",
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
                        "description": "Grants the ability to use SSH and "
                        "bypass all other permissions via "
                        "command line tools.",
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
                        "description": "This permission is only relevant if "
                        "your subscription has remote "
                        "administration.",
                        "group_label": "Administration",
                    },
                ]
            },
        }

        uri = f"{self.endpoint}/permissions"
        mocker.register_uri("GET", uri, json=response, status_code=200)
        permissions = self.acquia.permissions()
        self.assertIsInstance(permissions, PermissionsList)
