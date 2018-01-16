#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""{Desctiption}"""

import acapi2.exceptions
import os

from acapi2.resources.application import Application
from acapi2.resources.applicationlist import ApplicationList
from acapi2.resources.environment import Environment
from acapi2.resources.subscription import Subscription
from acapi2.resources.subscriptionlist import SubscriptionList


class Acquia(object):
    _api_endpoint = "https://cloud.acquia.com/api"

    def __init__(self,
                 api_key: str = None,
                 api_secret: str = None,
                 endpoint: str = None,
                 cache: int = 600) -> None:

        if endpoint:
            self._api_endpoint = endpoint

        if not api_key or not api_secret:
            api_key, api_secret = self.__find_credentials()
            if not api_key or not api_secret:
                msg = "Credentials not provided"
                raise acapi2.exceptions.AcquiaCloudException(msg)
        self._api_key = api_key
        self._api_secret = api_secret

    def applications(self,
                     filters: str = None,
                     sort: str = None,
                     limit: int = None,
                     offset: int = None) -> ApplicationList:
        qry_params = {
            "filter": filters,
            "sort": sort,
            "limit": limit,
            "offset": offset
        }

        apps = ApplicationList(self.api_endpoint, self.api_key,
                               self.api_secret, qry_params=qry_params)
        return apps

    def application(self, uuid) -> Application:
        namespace = "applications/" + uuid
        uri = self.get_uri(namespace)
        application = Application(uri, self.api_key,
                                  self.api_secret)
        return application

    def environment(self, env_id: str) -> Environment:
        namespace = "environments/" + str(env_id)
        uri = self.get_uri(namespace)
        return Environment(uri, self.api_key, self.api_secret)

    @property
    def api_endpoint(self) -> str:
        return self._api_endpoint

    @api_endpoint.setter
    def api_endpoint(self, endpoint: str):
        self._api_endpoint = endpoint

    @property
    def api_key(self) -> str:
        return self._api_key

    @api_key.setter
    def api_key(self, api_key: str):
        # TODO: validate api_key
        self._api_key = api_key

    @property
    def api_secret(self) -> str:
        return self._api_secret

    @api_secret.setter
    def api_secret(self, api_secret: str):
        # TODO: validate api_secret
        self._api_secret = api_secret

    def health(self):
        raise NotImplementedError

    def get_uri(self, path: str) -> str:
        uri = "{endpoint}/{path}".format(endpoint=self.api_endpoint,
                                         path=path)
        return uri

    def subscription(self, uuid: str) -> Subscription:
        namespace = "subscriptions/" + uuid
        uri = self.get_uri(namespace)
        subscription = Subscription(uri, self.api_key,
                                    self.api_secret)
        return subscription

    def subscriptions(self, filters: dict = None) -> SubscriptionList:
        subs = SubscriptionList(self.api_endpoint, self.api_key,
                                self.api_secret, filters=filters)
        return subs

    @staticmethod
    def __find_credentials() -> tuple:
        # TODO: This should go away.
        key = os.environ.get("ACQUIA_CLOUD_API_KEY")
        secret = os.environ.get("ACQUIA_CLOUD_API_SECRET")
        return key, secret
