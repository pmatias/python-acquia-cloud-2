#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia Applications resource"""

from acapi2.resources.acquialist import AcquiaList
from acapi2.resources.application import Application


class ApplicationList(AcquiaList):
    def __init__(self, uri: str, api_key: str, api_secret: str, *args,
                 **kwargs):
        # TODO Filters
        super().__init__(uri, api_key, api_secret, *args, **kwargs)
        self.fetch()

    def fetch(self):
        apps = super().request(uri=self.uri).json()
        try:
            app_items = apps["_embedded"]["items"]
        except KeyError:
            # TODO Handle this
            pass
        else:
            for app in app_items:
                app_id = app["uuid"]
                subs_uri = "{base_uri}/{uuid}".format(
                    base_uri=self.uri, uuid=app_id)
                self.__setitem__(app_id,
                                 Application(subs_uri,
                                             self.api_key,
                                             self.api_secret))

    @property
    def base_uri(self) -> str:
        return self._base_uri

    @base_uri.setter
    def base_uri(self, base_uri: str):
        uri = "{}/applications".format(base_uri)
        self._base_uri = uri
