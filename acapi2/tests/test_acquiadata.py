#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import os
import requests
import requests_mock
import unittest
import uuid

from acapi2.resources.acquiadata import AcquiaData
from acapi2.exceptions import *
from acapi2.tests import BaseTest


@requests_mock.Mocker()
class TestAcquiaData(unittest.TestCase):
    endpoint = "https://cloud.acquia.com/api/"

    # These api key and secret examples
    # were taken from the official API docs
    api_key = "d0697bfc-7f56-4942-9205-b5686bf5b3f5"
    api_secret = "D5UfO/4FfNBWn4+0cUwpLOoFzfP7Qqib4AoY+wYGsKE="

    def test_endpoint_not_found(self, mocker):
        uri = self.endpoint + "invalid/"

        mocker.register_uri("GET", uri, status_code=404)

        acquia_data = AcquiaData(
            uri, self.api_key, self.api_secret
        )

        with self.assertRaises(requests.HTTPError):
            acquia_data.request()

    def test_retry_and_get(self, mocker):
        mocker.register_uri("GET", self.endpoint,
                            [{"status_code": 500},
                             {"status_code": 503},
                             {"status_code": 502},
                             {"status_code": 200}])

        acquia_data = AcquiaData(
            self.endpoint, self.api_key, self.api_secret
        )

        self.assertEqual(acquia_data.request().status_code, 200)

    def test_unauthorised_request(self, mocker):
        mocker.register_uri("GET", self.endpoint, status_code=403)
        acquia_data = AcquiaData(
            self.endpoint, self.api_key, self.api_secret
        )

        with self.assertRaises(requests.HTTPError):
            acquia_data.request()

    def test_post_request(self, mocker): pass

    def test_delete_request(self, mocker): pass

    def test_badly_signed_headers(self, mocker): pass
