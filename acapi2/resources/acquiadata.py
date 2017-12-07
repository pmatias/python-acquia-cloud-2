#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia Cloud API Data network resource"""

import httphmac
import logging
import requests
import time
import uuid

from acapi2.version import __version__
from platform import python_version
from pprint import pformat

_logger = logging.getLogger("acapi2.resources.acquiadata")


class AcquiaData(object):
    _agent = 'Acquia Cloud API Client/{mver} (Python {pver})'
    _realm = _agent.format(mver=__version__,
                           pver=python_version())

    def __init__(self, uri: str, api_key: str, api_secret: str,
                 data: dict = None):
        self.uri = uri
        self.api_key = api_key
        self.api_secret = api_secret
        self.data = data
        self.last_response = None

    def request(self, uri: str = None, method: str = "GET",
                data: dict = None, params: dict = None):

        params = params or {}

        self.last_response = None

        if not uri:
            uri = self.uri

        response = None
        request = httphmac.Request()
        auth_headers = {
            "realm": self._realm,
            "id": self.api_key,
            "nonce": uuid.uuid4().hex,
            "version": "2.0"
        }
        request.with_url(uri).with_method(method)
        signer = httphmac.V2Signer()
        signer.sign_direct(request, auth_headers, self.api_secret)

        if "GET" == method:
            attempt = 0
            while attempt <= 5:
                # TODO: add params support in httphmac.Request()
                response = request.do()
                if response.status_code not in list(range(500, 505)):
                    break

                attempt += 1
                # this is not yet supported
                params["acapy_retry"] = attempt
                time.sleep((attempt ** 2.0) / 10)

            if "acapi_retry" in params:
                del params["acapi_retry"]

        if "POST" == method:
            response = request.with_json_body(data).do()

        if "DELETE" == method:
            response = request.do()

        self.last_response = response
        if response.status_code != requests.codes.ok \
                and response.status_code != requests.codes.accepted:
            try:
                raise response.raise_for_status()
            except requests.exceptions.HTTPError as exp:
                _logger.warning(
                    "Failed request response headers: \n%s",
                    pformat(exp.response.headers, indent=2))
                raise

        return response
