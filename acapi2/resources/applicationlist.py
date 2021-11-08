#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia Applications resource"""

from acapi2.exceptions import AcquiaCloudNoDataException
from acapi2.resources.acquialist import AcquiaList
from acapi2.resources.application import Application


class ApplicationList(AcquiaList):
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

    def fetch(self) -> None:
        apps = self.request(uri=self.uri, params=self._qry_params).json()
        try:
            app_items = apps["_embedded"]["items"]
        except KeyError:
            raise AcquiaCloudNoDataException()
        else:
            index = 0
            for app in app_items:
                subs_uri = app["_links"]["self"]["href"]
                self.__setitem__(
                    index, Application(subs_uri, self.api_key, self.api_secret)
                )
                index += 1

    @property
    def base_uri(self) -> str:
        return self._base_uri

    @base_uri.setter
    def base_uri(self, base_uri: str):
        self._base_uri = f"{base_uri}/applications"
