#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test Notification Endpoint"""

from unittest.mock import patch

import requests_mock

from acapi2.exceptions import (
    AcquiaCloudNotificationFailedException,
    AcquiaCloudTimeoutError,
)
from acapi2.resources.notification import Notification
from acapi2.tests import BaseTest
from acapi2.tests.util import load_fixture


@requests_mock.Mocker()
class TestNotification(BaseTest):
    def test_pending(self, mocker):
        response = load_fixture("acapi2/tests/fixtures/notification.json")

        notification_uuid = "1bd3487e-71d1-4fca-a2d9-5f969b3d35c1"
        uri = f"{self.endpoint}/notifications/{notification_uuid}"
        mocker.register_uri("GET", uri, status_code=200, json=response)
        is_pending = self.acquia.notification(notification_uuid).pending()
        assert is_pending

    @patch.object(Notification, "pending", return_value=True)
    def test_wait_in_progress(self, mocker, mock_pending):
        response = load_fixture("acapi2/tests/fixtures/notification.json")

        notification_uuid = "1bd3487e-71d1-4fca-a2d9-5f969b3d35c1"
        uri = f"{self.endpoint}/notifications/{notification_uuid}"
        mocker.register_uri("GET", uri, status_code=200, json=response)
        with self.assertRaises(AcquiaCloudTimeoutError):
            self.acquia.notification(notification_uuid).wait(5)

    @patch.object(Notification, "pending", return_value=False)
    def test_wait_failed(self, mocker, mock_pending):
        response = load_fixture(
            "acapi2/tests/fixtures/notification_failed.json"
        )

        notification_uuid = "1bd3487e-71d1-4fca-a2d9-5f969b3d35c1"
        uri = f"{self.endpoint}/notifications/{notification_uuid}"
        mocker.register_uri("GET", uri, status_code=200, json=response)
        with self.assertRaises(AcquiaCloudNotificationFailedException):
            self.acquia.notification(notification_uuid).wait(5)

    @patch.object(Notification, "pending", return_value=False)
    def test_wait_completed(self, mocker, mock_pending):
        response = load_fixture(
            "acapi2/tests/fixtures/notification_completed.json"
        )

        notification_uuid = "1bd3487e-71d1-4fca-a2d9-5f969b3d35c1"
        uri = f"{self.endpoint}/notifications/{notification_uuid}"
        mocker.register_uri("GET", uri, status_code=200, json=response)
        notification = self.acquia.notification(notification_uuid).wait(5)
        self.assertIsInstance(notification, Notification)
