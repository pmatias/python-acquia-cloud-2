#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia Environment resource"""

from acapi2.resources.acquialist import AcquiaList
from acapi2.resources.environment import Environment


class EnvironmentList(AcquiaList):
    def __init__(self, uri: str, api_key: str, api_secret: str, *args,
                 **kwargs):
        # TODO Filters
        super().__init__(uri, api_key, api_secret, *args, **kwargs)
        self.fetch()

    def fetch(self):
        # TODO should this method live in AcquiaList?
        envs = super().request(uri=self.uri).json()
        try:
            env_items = envs["_embedded"]["items"]
        except KeyError:
            # TODO Handle this
            pass
        else:
            for env in env_items:
                # The Acquia API is quite specific about this being
                # called id and not uuid :/
                env_id = env["id"]
                name = env["name"]
                envs_uri = "{base_uri}/{env_id}".format(
                    base_uri=self.uri, env_id=env_id)
                self.__setitem__(name,
                                 Environment(envs_uri,
                                             self.api_key,
                                             self.api_secret))

    @property
    def base_uri(self) -> str:
        return self._base_uri

    @base_uri.setter
    def base_uri(self, base_uri: str):
        uri = "{}/environments".format(base_uri)
        self._base_uri = uri
