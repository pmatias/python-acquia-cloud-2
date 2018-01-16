#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Environment resource"""

from acapi2.resources.acquiaresource import AcquiaResource
from requests.sessions import Session
from requests.exceptions import RequestException


class Environment(AcquiaResource):

    def code_switch(self, branch: str) -> Session:
        uri = self.uri + "/code/actions/switch"
        data = {
            "branch": branch
        }

        try:
            response = self.request(uri=uri, method="POST", data=data)
        except RequestException:
            print("There was an error on the request")
        else:
            return response

    def configure(self, data: dict) -> Session:
        return self.request(uri=self.uri, method="POST", data=data)

    def destroy(self):
        response = self.request(uri=self.uri, method="DELETE")

        return response

    def deploy_code(self, id_from: str) -> Session:
        uri = self.uri + "/code"
        data = {
            "source": id_from
        }

        try:
            response = self.request(uri=uri, method="POST", data=data)
        except RequestException:
            print("There was an error on the request")
        else:
            return response

    def deploy_database(self, id_from: str, db_name: str) -> None:
        uri = self.uri + "/databases"
        data = {
            "name": db_name,
            "source": id_from
        }

        try:
            response = self.request(uri=uri, method="POST", data=data)
        except RequestException:
            print("There was an error on the request")
        else:
            return response

    def set_php_version(self, version: str) -> Session:

        data = {
            "version": version
        }

        return self.configure(data)