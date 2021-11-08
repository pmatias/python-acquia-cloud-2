#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia Cloud API notifications."""

from acapi2.exceptions import AcquiaCloudNoDataException
from acapi2.resources.acquialist import AcquiaList
from acapi2.resources.notification import Notification


class NotificationList(AcquiaList):
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
        notifications = self.request(
            uri=self.uri, params=self._qry_params
        ).json()
        try:
            notif_items = notifications["_embedded"]["items"]
        except KeyError:
            raise AcquiaCloudNoDataException()
        else:
            for notification in notif_items:
                notif_uri = notification["_links"]["self"]["href"]
                self.__setitem__(
                    notification["uuid"],
                    Notification(notif_uri, self.api_key, self.api_secret),
                )

    @property
    def base_uri(self) -> str:
        return self._base_uri

    @base_uri.setter
    def base_uri(self, base_uri: str):
        self._base_uri = f"{base_uri}/notifications"
