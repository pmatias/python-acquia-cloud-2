#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia application resource."""
import requests

from acapi2.resources.acquiaresource import AcquiaResource
from acapi2.resources.environmentlist import EnvironmentList
from acapi2.resources.tasklist import TaskList


class Application(AcquiaResource):
    def artifacts(self):
        raise NotImplementedError

    def create_environment(self, label: str, branch: str,
                           databases: list = None) -> requests:
        if not databases:
            databases = ["database-" + branch]

        data = {
            "label": label,
            "branch": branch,
            "databases": databases
        }

        uri = "{}/environments".format(self.uri)
        response = self.request(uri=uri, method="POST", data=data)

        return response

    def environments(self, filters: dict = None):
        envs = EnvironmentList(self.uri, self.api_key,
                               self.api_secret, filters=filters)
        return envs

    def tasks(self, filters: dict = None):
        tasks = TaskList(self.uri, self.api_key,
                         self.api_secret, filters=filters)
        return tasks
