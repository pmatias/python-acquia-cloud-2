#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch

import requests
import requests_mock

from acapi2.http_request import HttpRequest
from acapi2.resources.acquiadata import AcquiaData


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

        acquia_data = AcquiaData(uri, self.api_key, self.api_secret)

        with self.assertRaises(requests.HTTPError):
            acquia_data.request()

    def test_retry_and_get(self, mocker):
        mocker.register_uri(
            "GET",
            self.endpoint,
            [
                {"status_code": 500},
                {"status_code": 503},
                {"status_code": 502},
                {"status_code": 200},
            ],
        )

        acquia_data = AcquiaData(self.endpoint, self.api_key, self.api_secret)

        self.assertEqual(acquia_data.request().status_code, 200)

    def test_unauthorised_request(self, mocker):
        mocker.register_uri("GET", self.endpoint, status_code=403)
        acquia_data = AcquiaData(self.endpoint, self.api_key, self.api_secret)

        with self.assertRaises(requests.HTTPError):
            acquia_data.request()

    def test_post_request(self, mocker):
        uri = self.endpoint + "organizations"
        mocker.register_uri(
            "POST",
            uri,
            status_code=200,
            json={"message": "Oganization created."},
        )

        acquia_data = AcquiaData(uri, self.api_key, self.api_secret)

        rdata = {"name": "A Random name"}
        response = acquia_data.request(method="POST", data=rdata)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"created", response.content)

    def test_delete_request(self, mocker):
        uri = self.endpoint + "organizations/1234"
        acquia_response = {
            "id": "6",
            "uuid": "g47ac10b-58cc-4372-a567-0e02b2c3d470",
            "name": "Sample organization",
            "subscriptions_total": "115",
            "admins_total": "2",
            "users_total": "82",
            "teams_total": "13",
            "roles_total": "4",
        }
        mocker.register_uri(
            "DELETE", uri, status_code=202, json=acquia_response
        )

        acquia_data = AcquiaData(uri, self.api_key, self.api_secret)
        response = acquia_data.request(method="DELETE")

        self.assertEqual(response.status_code, 202)
        self.assertIn(b"id", response.content)
        self.assertIn(b"name", response.content)

    @patch.object(HttpRequest, "do")
    def test_request_backoff(self, mocker, request_do_mock):
        request_do_mock.side_effect = [
            requests.exceptions.ConnectionError(),
            requests_mock.create_response(requests.Request()),
        ]

        acquia_data = AcquiaData(self.endpoint, self.api_key, self.api_secret)
        acquia_data.request()

        assert request_do_mock.call_count == 2
