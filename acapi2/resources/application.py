#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia application resource."""
from acapi2.resources.acquiaresource import AcquiaResource
from acapi2.resources.environment import Environment
from acapi2.resources.environmentlist import EnvironmentList
from acapi2.resources.tasklist import TaskList
from requests.sessions import Session


class Application(AcquiaResource):
    def artifacts(self):
        raise NotImplementedError

    def create_environment(self, label: str, branch: str,
                           databases: list = None) -> Session:
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

    def environments(self, filters: dict = None) -> EnvironmentList:
        envs = EnvironmentList(self.uri, self.api_key,
                               self.api_secret, filters=filters)
        return envs

    def environment(self, environment_id: str) -> Environment:
        # TODO resolve environment name instead?
        uri = "{base_uri}/environments/{env_id}".format(
            base_uri=self.uri,
            env_id=environment_id)
        env = Environment(uri, self.api_key, self.api_secret)
        return env

    def tasks(self, filters: dict = None):
        tasks = TaskList(self.uri, self.api_key,
                         self.api_secret, filters=filters)
        return tasks
