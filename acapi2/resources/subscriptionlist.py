#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia Subscriptions resource"""

from acapi2.resources.acquialist import AcquiaList
from acapi2.resources.subscription import Subscription


class SubscriptionList(AcquiaList):
    def __init__(
        self, uri: str, api_key: str, api_secret: str, *args, **kwargs
    ) -> None:
        # TODO Filters
        super().__init__(uri, api_key, api_secret, *args, **kwargs)
        self.fetch()

    def fetch(self):
        subs = self.request(uri=self.uri).json()
        try:
            sub_items = subs["_embedded"]["items"]
        except KeyError:
            # TODO Handle this
            pass
        else:
            for sub in sub_items:
                name = sub["id"]
                subs_uri = "{base_uri}/{uuid}".format(
                    base_uri=self.uri, uuid=name
                )
                self.__setitem__(
                    name, Subscription(subs_uri, self.api_key, self.api_secret)
                )

    @property
    def base_uri(self) -> str:
        return self._base_uri

    @base_uri.setter
    def base_uri(self, base_uri: str):
        uri = "{}/subscriptions".format(base_uri)
        self._base_uri = uri
