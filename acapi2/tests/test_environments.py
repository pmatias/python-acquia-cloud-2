#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test Acquia Environments"""

import requests_mock

from acapi2.tests import BaseTest


@requests_mock.Mocker()
class TestEnvironments(BaseTest):
    def test_destroy_env(self, mocker):
        app_uuid = "a47ac10b-58cc-4372-a567-0e02b2c3d470"
        env_id = "24-a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/applications/{uuid}/{env_id}"
        uri = uri.format(base_uri=self.endpoint, uuid=app_uuid,
                         env_id=env_id)
        response = {
            "message": "The environment is being deleted."
        }

        mocker.register_uri(url=uri, method="DELETE",
                            status_code=202, json=response)

        response = self.acquia.application(app_uuid). \
            environment(env_id).destroy()

        self.assertEqual(response.status_code, 202)
