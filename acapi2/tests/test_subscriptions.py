#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Subscriptions tests"""

import requests_mock

from acapi2.resources.applicationlist import ApplicationList
from acapi2.resources.subscriptionlist import SubscriptionList
from acapi2.tests import BaseTest


@requests_mock.Mocker()
class TestSubscriptions(BaseTest):
    def test_subscription_list(self, mocker):
        response = {
            "total": 3,
            "_links": {
                "self": {"href": "{baseUri}/subscriptions"},
                "sort": {
                    "href": "{baseUri}/subscriptions{?sort}",
                    "templated": True,
                },
                "filter": {
                    "href": "{baseUri}/subscriptions{?filter}",
                    "templated": True,
                },
                "limit": {
                    "href": "{baseUri}/subscriptions{?limit}",
                    "templated": True,
                },
                "parent": {"href": "{baseUri}"},
            },
            "_embedded": {
                "items": [
                    {
                        "id": 123,
                        "uuid": "a1aaa1aa-aa11-aaa1" "-11aa-123456789012",
                        "name": "Acquia Cloud Free Subscription",
                        "start_at": "2011-03-28T00:00:00",
                        "expire_at": "2015-11-11T00:00:00",
                        "product": {
                            "id": 1890149,
                            "name": "Acquia Cloud Free",
                            "type": "free",
                        },
                        "applications_total": 3,
                        "applications_used": 1,
                        "advisory_hours_total": 1.23,
                        "advisory_hours_used": 4.56,
                        "organization": {
                            "uuid": "g1ggg1gg-" "gg11-ggg1-11gg-123456789012",
                            "name": "Acquia Inc.",
                        },
                        "flags": {
                            "active": True,
                            "expired": False,
                            "zuora": False,
                        },
                        "_links": {
                            "self": {
                                "href": "{baseUri}/subscriptions/"
                                "a1aaa1aa-aa11"
                                "-aaa1-11aa-123456789012"
                            }
                        },
                    },
                    {
                        "id": 222,
                        "uuid": "b1bbb1bb-bb11-bbb1-" "11bb-123456789012",
                        "name": "My Acquia Subscription",
                        "start_at": "2012-05-15T12:00:00Z",
                        "expire_at": "2015-05-15T12:00:00Z",
                        "product": {
                            "id": 8999,
                            "name": "Enterprise",
                            "type": "enterprise",
                        },
                        "applications_total": 5,
                        "applications_used": 2,
                        "advisory_hours_total": 2.34,
                        "advisory_hours_used": 5.67,
                        "organization": {
                            "uuid": "g2ggg2gg-gg22-ggg2-" "22gg-123456789012",
                            "name": "My Organization",
                        },
                        "flags": {
                            "active": True,
                            "expired": False,
                            "zuora": False,
                        },
                        "_links": {
                            "self": {
                                "href": "{baseUri}/subscriptions/"
                                "b1bbb1bb-bb11"
                                "-bbb1-11bb-123456789012"
                            }
                        },
                    },
                    {
                        "id": 333,
                        "uuid": "c1ccc1cc-cc11-ccc1" "-11cc-123456789012",
                        "name": "My Acquia Subscription 2",
                        "start_at": "2012-05-15T12:00:00Z",
                        "expire_at": "2015-05-15T12:00:00Z",
                        "product": {
                            "id": 8999,
                            "name": "Enterprise",
                            "type": "enterprise",
                        },
                        "applications_total": 5,
                        "applications_used": 2,
                        "advisory_hours_total": 3.45,
                        "advisory_hours_used": 6.78,
                        "organization": {
                            "uuid": "g2ggg2gg-gg22-" "ggg2-22gg-123456789012",
                            "name": "My Organization",
                        },
                        "flags": {
                            "active": True,
                            "expired": False,
                            "zuora": False,
                        },
                        "_links": {
                            "self": {
                                "href": "{baseUri}/subscriptions/"
                                "c1ccc1cc-cc11-"
                                "ccc1-11cc-123456789012"
                            }
                        },
                    },
                ]
            },
        }

        uri = "{}/subscriptions".format(self.endpoint)
        mocker.register_uri("GET", uri, json=response, status_code=200)

        subscriptions = self.acquia.subscriptions()
        self.assertIsInstance(subscriptions, SubscriptionList)

    def test_subscription_applications(self, mocker):
        response = {
            "total": 2,
            "pagination": {"total": 2, "limit": 10, "offset": 0},
            "_links": {
                "self": {
                    "href": "{baseUri}/subscriptions/abcdef12-1234"
                    "-4372-a567-0e02b2c3d470/applications"
                },
                "parent": {
                    "href": "{baseUri}/subscriptions/abcdef12-1234"
                    "-4372-a567-0e02b2c3d470"
                },
                "sort": {
                    "href": "{baseUri}/subscriptions/abcdef12-1234"
                    "-4372-a567-0e02b2c3d470/"
                    "applications{?sort}",
                    "templated": True,
                },
                "filter": {
                    "href": "{baseUri}/subscriptions/abcdef12-1234"
                    "-4372-a567-0e02b2c3d470/"
                    "applications{?filter}",
                    "templated": True,
                },
                "limit": {
                    "href": "{baseUri}/subscriptions/abcdef12-1234"
                    "-4372-a567-0e02b2c3d470/"
                    "applications{?limit}",
                    "templated": True,
                },
            },
            "_embedded": {
                "items": [
                    {
                        "id": 241643,
                        "uuid": "a47ac10b-58cc-4372-" "a567-0e02b2c3d470",
                        "name": "Sample application 1",
                        "hosting": {"type": "acp", "id": "devcloud:devcloud2"},
                        "subscription": {
                            "uuid": "s47ac10b-58cc-4372-" "a567-0e02b2c3d470",
                            "name": "Sample subscription",
                        },
                        "organization": {
                            "uuid": "g47ac10b-58cc-4372-" "a567-0e02b2c3d470",
                            "name": "Sample organization",
                        },
                        "flags": {"remote_admin": True},
                        "status": "normal",
                        "_links": {
                            "self": {
                                "href": "{baseUri}/applications/"
                                "a47ac10b-58cc-4372"
                                "-a567-0e02b2c3d470"
                            }
                        },
                    },
                    {
                        "id": 954291,
                        "uuid": "a47ac10b-58cc-4372" "-a567-0e02b2c3d471",
                        "name": "Sample application 2",
                        "hosting": {
                            "type": "free",
                            "id": "devcloud:devcloud2",
                        },
                        "subscription": {
                            "uuid": "s47ac10b-58cc-4372" "-a567-0e02b2c3d470",
                            "name": "Sample subscription",
                        },
                        "organization": {
                            "uuid": "g47ac10b-58cc-4372" "-a567-0e02b2c3d470",
                            "name": "Sample organization",
                        },
                        "flags": {"remote_admin": False},
                        "status": "provisioning",
                        "_links": {
                            "self": {
                                "href": "{baseUri}/applications/"
                                "a47ac10b-58cc-4372"
                                "-a567-0e02b2c3d471"
                            }
                        },
                    },
                ]
            },
        }

        uuid = "a47ac10b-58cc-4372-a567-0e02b2c3d470"
        uri = "{base_uri}/subscriptions/{uuid}/applications".format(
            base_uri=self.endpoint, uuid=uuid
        )
        mocker.register_uri("GET", uri, json=response, status_code=200)

        applications = self.acquia.subscription(uuid).applications()
        self.assertIsInstance(applications, ApplicationList)
