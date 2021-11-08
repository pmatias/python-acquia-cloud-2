#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Tasks tests"""

import requests_mock

from acapi2.resources.tasklist import TaskList
from acapi2.tests import BaseTest


@requests_mock.Mocker()
class TestTasks(BaseTest):
    def test_get_application_tasks(self, mocker):
        response = {
            "total": 2,
            "_links": {
                "self": {
                    "href": "{baseUri}/applications/0c7e79ab-1c4a"
                    "-424e-8446-76ae8be7e851/tasks"
                },
                "parent": {
                    "href": "{baseUri}/applications/0c7e79ab-1c4a"
                    "-424e-8446-76ae8be7e851"
                },
            },
            "_embedded": {
                "items": [
                    {
                        "progress": 0,
                        "user": {
                            "uuid": "a18a1d80-8896-11e1" "-9eb5-12313928d5b8",
                            "first_name": "James",
                            "last_name": "Kirk",
                            "mail": "james.kirk@example.com",
                            "picture_url": "https://accounts.acquia.com/"
                            "path/to/imagepng",
                            "username": "james.kirk",
                        },
                        "uuid": "53098518-0da8-4e41" "-943b-1198e3614f38",
                        "name": "OperationStarted",
                        "title": "Operation title",
                        "description": "Operation description.",
                        "created_at": "2017-04-04T17:21:53-04:00",
                        "started_at": "2017-04-04T17:21:53-04:00",
                        "completed_at": "2017-04-04T17:21:59-04:00",
                        "status": "started",
                        "type": "task",
                        "metadata": {
                            "environment": {
                                "ids": [
                                    "63-0c7e79ab-1c4a"
                                    "-424e-8446-76ae8be7e851"
                                ]
                            }
                        },
                        "labels": ["database", "hosting"],
                        "reference_uuid": "53098518-0da8-4e41"
                        "-943b-1198e3614f38",
                        "_links": {
                            "self": {
                                "href": "{baseUri}/applications/"
                                "0c7e79ab-1c4a-424e-8446"
                                "-76ae8be7e851/tasks"
                            }
                        },
                    },
                    {
                        "progress": 100,
                        "user": {
                            "uuid": "a18a1d80-8896-11e1" "-9eb5-12313928d5b8",
                            "first_name": "James",
                            "last_name": "Kirk",
                            "mail": "james.kirk@example.com",
                            "picture_url": "https://accounts.acquia.com/"
                            "path/to/imagepng",
                            "username": "james.kirk",
                        },
                        "uuid": "63098518-0da8-4e41" "-943b-1198e3614f38",
                        "name": "OperationStarted",
                        "title": "Operation title",
                        "description": "Operation description.",
                        "created_at": "2017-04-04T17:21:53-04:00",
                        "started_at": "2017-04-04T17:21:53-04:00",
                        "completed_at": "2017-04-04T17:21:59-04:00",
                        "status": "completed",
                        "type": "task",
                        "metadata": {
                            "environment": {
                                "ids": [
                                    "63-0c7e79ab-1c4a"
                                    "-424e-8446-76ae8be7e851"
                                ]
                            }
                        },
                        "labels": ["database", "hosting"],
                        "reference_uuid": "53098518-0da8-4e41"
                        "-943b-1198e3614f38",
                        "_links": {
                            "self": {
                                "href": "{baseUri}/applications/"
                                "0c7e79ab-1c4a-424e"
                                "-8446-76ae8be7e851/tasks"
                            }
                        },
                    },
                ]
            },
        }

        app_uuid = "0c7e79ab-1c4a-424e-8446-76ae8be7e851"
        uri = "{base_uri}/applications/{uuid}/tasks".format(
            base_uri=self.endpoint, uuid=app_uuid
        )
        mocker.register_uri("GET", uri, json=response, status_code=200)
        tasks = self.acquia.application(app_uuid).tasks()
        self.assertIsInstance(tasks, TaskList)

    def test_wait_task(self, mocker):
        pass

    def test_failed_task(self, mocker):
        pass

    def test_task_not_found(self, mocker):
        pass
