#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia Main Object"""
import os

from acapi2.exceptions import AcquiaCloudException
from acapi2.resources.agreement import Agreement
from acapi2.resources.agreementlist import AgreementList
from acapi2.resources.application import Application
from acapi2.resources.applicationlist import ApplicationList
from acapi2.resources.environment import Environment
from acapi2.resources.notification import Notification
from acapi2.resources.permissionslist import PermissionsList
from acapi2.resources.subscription import Subscription
from acapi2.resources.subscriptionlist import SubscriptionList


class Acquia(object):
    _api_endpoint = "https://cloud.acquia.com/api"

    def __init__(
        self, api_key: str = None, api_secret: str = None, endpoint: str = None
    ) -> None:

        if endpoint:
            self._api_endpoint = endpoint

        if not api_key or not api_secret:
            api_key, api_secret = self.__find_credentials()
            if not api_key or not api_secret:
                msg = "Credentials not provided"
                raise AcquiaCloudException(msg)

        self._api_key = api_key
        self._api_secret = api_secret

    def agreements(self) -> AgreementList:
        return AgreementList(self.api_endpoint, self.api_key, self.api_secret)

    def agreement(self, uuid) -> Agreement:
        namespace = f"agreements/{uuid}"
        uri = self.get_uri(namespace)
        return Agreement(uri, self.api_key, self.api_secret)

    def applications(
        self,
        filters: str = None,
        sort: str = None,
        limit: int = None,
        offset: int = None,
    ) -> ApplicationList:
        qry_params = {
            "filter": filters,
            "sort": sort,
            "limit": limit,
            "offset": offset,
        }

        apps = ApplicationList(
            self.api_endpoint,
            self.api_key,
            self.api_secret,
            qry_params=qry_params,
        )
        return apps

    def application(self, uuid: str) -> Application:
        namespace = f"applications/{uuid}"
        uri = self.get_uri(namespace)
        application = Application(uri, self.api_key, self.api_secret)
        return application

    def notification(self, uuid: str) -> Notification:
        namespace = f"notifications/{uuid}"
        uri = self.get_uri(namespace)
        return Notification(uri, self.api_key, self.api_secret)

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
        return f"{self.api_endpoint}/{path}"

    def permissions(self) -> PermissionsList:
        return PermissionsList(
            self.api_endpoint, self.api_key, self.api_secret
        )

    def subscription(self, uuid: str) -> Subscription:
        namespace = "subscriptions/" + uuid
        uri = self.get_uri(namespace)
        subscription = Subscription(uri, self.api_key, self.api_secret)
        return subscription

    def subscriptions(self, filters: dict = None) -> SubscriptionList:
        subs = SubscriptionList(
            self.api_endpoint, self.api_key, self.api_secret, filters=filters
        )
        return subs

    @staticmethod
    def __find_credentials() -> tuple:
        key = os.environ.get("ACQUIA_CLOUD_API_KEY")
        secret = os.environ.get("ACQUIA_CLOUD_API_SECRET")
        return key, secret
