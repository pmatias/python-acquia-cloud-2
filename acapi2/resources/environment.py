#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Environment resource"""

from acapi2.resources.acquiaresource import AcquiaResource
from requests.sessions import Session


class Environment(AcquiaResource):

    def code_switch(self, branch_tag: str) -> Session:
        uri = self.uri + "/code/actions/switch"
        data = {
            "branch": branch_tag
        }

        response = self.request(uri=uri, method="POST", data=data)
        return response

    def configure(self, data: dict) -> Session:
        return self.request(uri=self.uri, method="PUT", data=data)

    def create_domain(self, domain: str) -> Session:
        uri = self.uri + "/domains"
        data = {
            "hostname": domain
        }
        response = self.request(uri=uri, method="POST", data=data)

        return response

    def create_log_forwarding_destinations(
        self,
        label: str,
        sources: list,
        consumer: str,
        credentials: dict,
        address: str
    ) -> Session:
        uri = self.uri + "/log-forwarding-destinations"
        data = {
            "label": label,
            "sources": sources,
            "consumer": consumer,
            "credentials": credentials,
            "address": address
        }
        response = self.request(uri=uri, method="POST", data=data)

        return response

    def delete_domain(self, domain: str) -> Session:
        uri = self.uri + "/domains/{domain}".format(domain=domain)
        response = self.request(uri=uri, method="DELETE")

        return response

    def clear_varnish_domain(self, domain: str) -> Session:
        uri = self.uri + \
            "/domains/{domain}/actions/clear-varnish".format(domain=domain)
        data = {
            "hostname": domain
        }
        response = self.request(uri=uri, method="POST", data=data)

        return response

    def destroy(self):
        response = self.request(uri=self.uri, method="DELETE")

        return response

    def deploy_code(self, id_from: str) -> Session:
        uri = self.uri + "/code"
        data = {
            "source": id_from
        }

        response = self.request(uri=uri, method="POST", data=data)
        return response

    def deploy_database(self, id_from: str, db_name: str) -> None:
        uri = self.uri + "/databases"
        data = {
            "name": db_name,
            "source": id_from
        }

        response = self.request(uri=uri, method="POST", data=data)
        return response

    def deploy_files(self, id_from: str) -> Session:
        uri = self.uri + "/files"
        data = {
            "source": id_from
        }

        response = self.request(uri=uri, method="POST", data=data)
        return response

    def get_crons(self) -> dict:
        uri = self.uri + "/crons"

        response = self.request(uri=uri)
        return response.json()

    def get_log_forwarding_destinations(self) -> dict:
        uri = self.uri + "/log-forwarding-destinations"

        response = self.request(uri=uri)
        return response.json()

    def get_servers(self) -> dict:
        uri = self.uri + "/servers"

        response = self.request(uri=uri)
        return response.json()

    def get_php_version(self) -> dict:
        uri = self.uri + "/"

        response = self.request(uri=uri)
        env_config = response.json()
        return {'php_version': env_config['configuration']['php']['version']}

    def set_php_version(self, version: str) -> Session:

        data = {
            "version": version
        }

        return self.configure(data)
