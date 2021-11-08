#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia Cloud API Data network resource"""
import logging
import time
import uuid
from platform import python_version
from pprint import pformat
from urllib.parse import urlencode

import backoff
import httphmac
import requests

from acapi2.http_request import HttpRequest
from acapi2.version import __version__

_logger = logging.getLogger("acapi2.resources.acquiadata")


class AcquiaData(object):
    _agent = "Acquia Cloud API Client/{mver} (Python {pver})"
    _realm = _agent.format(mver=__version__, pver=python_version())

    def __init__(
        self, uri: str, api_key: str, api_secret: str, data: dict = None
    ) -> None:
        self.uri = uri
        self.api_key = api_key
        self.api_secret = api_secret
        self._data = data or {}
        self.last_response: requests.Response = requests.Response()

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data: dict):
        self._data = data

    @staticmethod
    def generate_url_query(uri: str, params: dict) -> str:
        # TODO: add params support in httphmac.Request()
        qry = urlencode(params)
        url = "{uri}?{qry}".format(uri=uri, qry=qry)
        return url

    @backoff.on_exception(
        backoff.expo, requests.exceptions.RequestException, max_time=10
    )
    def request(
        self,
        uri: str = None,
        method: str = "GET",
        data: dict = None,
        params: dict = None,
    ):

        if not uri:
            uri = self.uri

        if params:
            params = {k: v for k, v in params.items() if v is not None}
            uri = self.generate_url_query(uri, params)

        response: requests.Response
        request = HttpRequest()
        auth_headers = {
            "realm": self._realm,
            "id": self.api_key,
            "nonce": uuid.uuid4().hex,
            "version": "2.0",
        }
        request.with_url(uri).with_method(method).with_time()
        signer = httphmac.V2Signer()
        signer.sign_direct(request, auth_headers, self.api_secret)

        if "GET" == method:
            attempt = 0
            while attempt <= 5:
                response = request.do()
                if response.status_code not in list(range(500, 505)):
                    break

                attempt += 1
                time.sleep((attempt ** 2.0) / 10)

        if "POST" == method or "PUT" == method:
            request.with_json_body(data)
            signer.sign_direct(request, auth_headers, self.api_secret)
            response = request.do()
            logging.debug(response.content)

        if "DELETE" == method:
            response = request.do()
            logging.debug(response.content)

        self.last_response = response
        if (
            response.status_code != requests.codes.ok
            and response.status_code != requests.codes.accepted
        ):
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as exp:
                _logger.warning(
                    "Failed request response headers: \n%s",
                    pformat(exp.response.headers, indent=2),
                )
                raise

        return response
