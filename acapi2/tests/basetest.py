#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""ACAPI2 Tests."""
import unittest

import requests
import requests_mock

from acapi2 import Acquia


class BaseTest(unittest.TestCase):
    acquia = None

    def setUp(self):
        self.endpoint = "https://cloud.acquia.com/api"

        # These api key and secret examples
        # were taken from the official API docs
        api_key = "d0697bfc-7f56-4942-9205-b5686bf5b3f5"
        api_secret = "D5UfO/4FfNBWn4+0cUwpLOoFzfP7Qqib4AoY+wYGsKE="

        session = requests.session()
        adapter = requests_mock.Adapter()

        session.mount("mock", adapter)
        self.acquia = Acquia(api_key, api_secret)
