#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test Notifications Endpoint"""

import requests_mock

from acapi2.resources.notificationlist import NotificationList
from acapi2.tests import BaseTest


@requests_mock.Mocker()
class TestNotifications(BaseTest):
    def test_notifications(self, mocker):
        response = {
            "_embedded": {
                "items": [
                    {
                        "_embedded": {
                            "author": {
                                "created_at": "2019-11-25T14:07:44+00:00",
                                "email": "some@email.com",
                                "first_name": "Name",
                                "last_login_at": "2020-02-07T12:24:29+00:00",
                                "last_name": "Ue",
                                "picture_url": "https://accounts.acquia.com/"
                                "images/users/f0886584-0830-55"
                                "5d-c234-14ffde052431/"
                                "style/avatar",
                                "username": "username",
                                "uuid": "f0886584-0830-555d-c234-"
                                "14ffde052431",
                            }
                        },
                        "_links": {
                            "parent": {
                                "href": "https://cloud.acquia.com/api"
                                "/notifications"
                            },
                            "self": {
                                "href": "https://cloud.acquia.com/api/"
                                "notifications/1bd3487e-71d1-4fca-a2d9"
                                "-5f969b3d35c1"
                            },
                        },
                        "completed_at": "2020-02-06T13:33:08+00:00",
                        "created_at": "2020-02-06T13:31:48+00:00",
                        "description": "Log forwarding destination created on Dev.",
                        "event": "LogForwardingDestinationCreated",
                        "label": "Log forwarding destination created",
                        "progress": 100,
                        "status": "completed",
                        "uuid": "1bd3487e-71d1-4fca-a2d9-5f969b3d35c1",
                    }
                ]
            },
            "_links": {
                "filter": {
                    "href": "https://cloud.acquia.com/api/applications/"
                    "f027502b-ed6c-448e-97e8-4a0def7d25e1/"
                    "notifications{?filter}",
                    "templated": True,
                },
                "limit": {
                    "href": "https://cloud.acquia.com/api/"
                    "applications/f027502b-ed6c-448e-97e8-"
                    "4a0def7d25e1/notifications{?limit}",
                    "templated": True,
                },
                "next": {
                    "href": "https://cloud.acquia.com/api/applications/"
                    "f027502b-ed6c-448e-97e8-4a0def7d25e1/"
                    "notifications?limit=2&offset=2"
                },
                "offset": {
                    "href": "https://cloud.acquia.com/api/applications/"
                    "f027502b-ed6c-448e-97e8-4a0def7d25e1/"
                    "notifications{?offset}",
                    "templated": True,
                },
                "parent": {
                    "href": "https://cloud.acquia.com/api/applications/"
                    "f027502b-ed6c-448e-97e8-4a0def7d25e1?limit=2"
                },
                "self": {
                    "href": "https://cloud.acquia.com/api/applications/"
                    "f027502b-ed6c-448e-97e8-4a0def7d25e1/"
                    "notifications?limit=2"
                },
                "sort": {
                    "href": "https://cloud.acquia.com/api/applications/"
                    "f027502b-ed6c-448e-97e8-4a0def7d25e1/"
                    "notifications{?sort}",
                    "templated": True,
                },
            },
            "pagination": {"limit": 2, "offset": 0, "total": "81"},
            "total": "81",
        }

        app_uuid = "f027502b-ed6c-448e-97e8-4a0def7d25e1"
        uri = f"{self.endpoint}/applications/{app_uuid}/notifications"
        mocker.register_uri("GET", uri, status_code=200, json=response)
        notif = self.acquia.application(app_uuid).notifications()

        self.assertIsInstance(notif, NotificationList)
