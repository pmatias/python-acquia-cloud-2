#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests_mock
import os

from acapi2 import Acquia
from acapi2.tests import BaseTest
from acapi2.exceptions import AcquiaCloudException


@requests_mock.Mocker()
class TestAcquia(BaseTest):
    def test_failed_connection(self, mocker): pass

    def test_wrong_credentials_connection(self, mocker): pass

    def test_connection_system_health(self, mocker): pass

    def test_missing_os_credentials(self, mocker: object):
        os.environ["ACQUIA_CLOUD_API_KEY"] = ""
        os.environ["ACQUIA_CLOUD_API_SECRET"] = ""

        with self.assertRaises(AcquiaCloudException) as context:
            Acquia()

        self.assertEqual(str(context.exception),
                         "Credentials not provided")
