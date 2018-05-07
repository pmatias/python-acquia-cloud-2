#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia application resource."""
from acapi2.resources.acquiaresource import AcquiaResource
from acapi2.resources.environment import Environment
from acapi2.resources.environmentlist import EnvironmentList
from acapi2.resources.tasklist import TaskList
from requests.sessions import Session
from requests.exceptions import RequestException


class Application(AcquiaResource):
    def artifacts(self):
        raise NotImplementedError

    def create_database(self, name: str) -> Session:
        uri = "{}/databases".format(self.uri)
        data = {
            "name": name
        }

        response = None
        try:
            response = self.request(uri=uri, method="POST", data=data)
        except RequestException:
            print("There was an error in the request.")

        return response

    def create_environment(self, label: str, env_name: str,
                           databases: list = None) -> Session:
        if not databases:
            databases = ["database_" + env_name]

        data = {
            "label": label,
            "branch": env_name,
            "databases": databases
        }

        uri = "{}/environments".format(self.uri)

        response = None
        try:
            response = self.request(uri=uri,
                                    method="POST", data=data)
        except RequestException:
            print("There was an error in the request.")

        return response

    def environments(self,
                     filters: dict = None,
                     sort: str = None,
                     limit: int = None,
                     offset: int = None) -> EnvironmentList:

        qry_params = {
            "filters": filters,
            "sort": sort,
            "limit": limit,
            "offset": offset
        }

        envs = EnvironmentList(self.uri, self.api_key,
                               self.api_secret, qry_params=qry_params)
        return envs

    def environment(self, environment_id: str) -> Environment:
        uri = "{base_uri}/{env_id}".format(
            base_uri=self.uri,
            env_id=environment_id)
        env = Environment(uri, self.api_key, self.api_secret)
        return env

    def load(self) -> None:
        self.populate_data()

    def tasks(self, filters: dict = None):
        tasks = TaskList(self.uri, self.api_key,
                         self.api_secret, filters=filters)
        return tasks
