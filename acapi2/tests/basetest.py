#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""ACAPI2 Tests."""
import requests
import requests_mock
import unittest

from acapi2 import Acquia


class BaseTest(unittest.TestCase):

    acquia = None

    def SetUp(self):

        session = requests.session()
        adapter = requests_mock.Adapter()

        session.mount("mock", adapter)
        self.acquia = Acquia("testKey", "testToken", cache=None)