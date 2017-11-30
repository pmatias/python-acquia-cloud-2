#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""{Desctiption}"""

import acapi2.exceptions
import os


class Acquia(object):

    _api_endpoint = "https://cloud.acquia.com/api"

    def __init__(self,
                 key: str = None,
                 secret: str = None,
                 endpoint: str = None,
                 cache: int = 600):

        if endpoint:
            self._api_endpoint = endpoint

        if not key or not secret:
            key, secret = self.__find_credentials()
            if not key or not secret:
                msg = "Credentials not provided"
                raise acapi2.exceptions.AcquiaCloudException(msg)

    @staticmethod
    def __find_credentials():
        key = os.environ.get("ACQUIA_CLOUD_API_KEY")
        secret = os.environ.get("ACQUIA_CLOUD_API_SECRET")
        return key, secret

