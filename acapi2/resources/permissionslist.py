#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Permissions API Endpoint"""

from acapi2.exceptions import AcquiaCloudNoDataException
from acapi2.resources.acquialist import AcquiaList


class PermissionsList(AcquiaList):
    def __init__(
        self, uri: str, api_key: str, api_secret: str, *args, **kwargs
    ) -> None:
        super().__init__(uri, api_key, api_secret, *args, **kwargs)
        self.fetch()

    def fetch(self) -> None:
        perms = self.request(uri=self.uri).json()

        try:
            perm_items = perms["_embedded"]["items"]
        except KeyError:
            raise AcquiaCloudNoDataException
        else:
            for perm in perm_items:
                name = perm["name"]
                self.__setitem__(name, perm)

    @property
    def base_uri(self) -> str:
        return self._base_uri

    @base_uri.setter
    def base_uri(self, base_uri: str):
        self._base_uri = f"{base_uri}/permissions"
