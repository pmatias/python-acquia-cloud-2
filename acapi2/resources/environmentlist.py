#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia Environment resource"""

from acapi2.exceptions import AcquiaCloudNoDataException
from acapi2.resources.acquialist import AcquiaList


class EnvironmentList(AcquiaList):
    def __init__(
        self,
        uri: str,
        api_key: str,
        api_secret: str,
        qry_params: dict = None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(uri, api_key, api_secret, *args, **kwargs)
        self._qry_params = qry_params
        self.fetch()

    def fetch(self):
        envs = self.request(uri=self.uri, params=self._qry_params).json()
        try:
            env_items = envs["_embedded"]["items"]
        except KeyError:
            raise AcquiaCloudNoDataException
        else:
            for env in env_items:
                name = env["name"]
                self.__setitem__(name, env)

    @property
    def base_uri(self) -> str:
        return self._base_uri

    @base_uri.setter
    def base_uri(self, base_uri: str):
        self._base_uri = f"{base_uri}/environments"
