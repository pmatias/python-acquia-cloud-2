#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia application resource."""
from requests.exceptions import RequestException
from requests.sessions import Session

from acapi2.resources.acquiaresource import AcquiaResource
from acapi2.resources.environment import Environment
from acapi2.resources.environmentlist import EnvironmentList
from acapi2.resources.notificationlist import NotificationList
from acapi2.resources.tasklist import TaskList


class Application(AcquiaResource):
    def artifacts(self):
        raise NotImplementedError

    def create_database(self, name: str) -> Session:
        uri = f"{self.uri}/databases"
        data = {"name": name}

        response = Session()
        try:
            response = self.request(uri=uri, method="POST", data=data)
        except RequestException:
            print("There was an error in the request.")

        return response

    def create_environment(
        self, label: str, env_name: str, databases: list = None
    ) -> Session:
        if not databases:
            databases = ["database_" + env_name]

        data = {"label": label, "branch": env_name, "databases": databases}

        uri = f"{self.uri}/environments"

        response = Session()
        try:
            response = self.request(uri=uri, method="POST", data=data)
        except RequestException:
            print("There was an error in the request.")

        return response

    def environments(
        self,
        filters: dict = None,
        sort: str = None,
        limit: int = None,
        offset: int = None,
    ) -> EnvironmentList:

        qry_params = {
            "filter": filters,
            "sort": sort,
            "limit": limit,
            "offset": offset,
        }

        return EnvironmentList(
            self.uri, self.api_key, self.api_secret, qry_params=qry_params
        )

    def environment(self, environment_id: str) -> Environment:
        uri = f"{self.uri}/{environment_id}"
        return Environment(uri, self.api_key, self.api_secret)

    def load(self) -> None:
        self.populate_data()

    def notifications(
        self,
        filters: dict = None,
        sort: str = None,
        limit: int = None,
        offset: int = None,
    ) -> NotificationList:
        """Get the notifications for this tasks."""

        qry_params = {
            "filter": filters,
            "sort": sort,
            "limit": limit,
            "offset": offset,
        }

        return NotificationList(
            self.uri, self.api_key, self.api_secret, qry_params=qry_params
        )

    def permissions(self) -> Session:
        uri = f"{self.uri}/permissions"

        response = Session()
        try:
            response = self.request(uri=uri, method="GET")
        except RequestException:
            print("There was an error in the request.")

        return response

    def tasks(self, filters: dict = None) -> TaskList:
        """DEPRECATED(use notifications): Get tasks for this application."""
        return TaskList(
            self.uri, self.api_key, self.api_secret, filters=filters
        )
