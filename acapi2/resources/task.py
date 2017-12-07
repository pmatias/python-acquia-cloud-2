#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia API task queue resource."""
import logging
import re
import requests_cache
import time

from datetime import datetime, timedelta

from acapi2.exceptions import AcquiaCloudTaskFailedException
from acapi2.resources.acquiaresource import AcquiaResource

LOGGER = logging.getLogger('acapi2.resources.task')


class Task(AcquiaResource):
    POLL_INTERVAL = 3

    def __init__(self, uri: str, api_key: str, api_secret: str,
                 data: dict = None) -> None:
        self.loops = 0
        super().__init__(uri, api_key, api_secret, data)

    def mangle_uri(self, uri: str, task_data: dict):
        raise NotImplementedError

    def is_pending(self) -> bool:
        with requests_cache.disabled():
            task = self.request().json()["embedded"]["_items"]

        self.data = task
        return task["progress"] is not 100

    def wait(self, timeout: int = 1000) -> "Task":
        start = datetime.now()
        max_time = start + timedelta(seconds=timeout)

        while self.is_pending():
            if start >= max_time:
                msg = "Time out exceeded while waiting for {}".format(
                    self.data["uuid"])
                raise AcquiaCloudTaskFailedException(msg, self.data)
            time.sleep(self.POLL_INTERVAL)

        task = self.get()
        # TODO We may have to inquiry Acquia for the new statuses
        if task["status"] is not "completed":
            msg = "Task {} failed".format(self.data["uuid"])
            raise AcquiaCloudTaskFailedException(msg, task)

        end = datetime.now()
        delta = end - start

        LOGGER.info("Waited %.2f seconds for task to complete",
                    delta.total_seconds())

        return self
