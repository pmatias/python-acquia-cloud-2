#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia API task queue resource."""
import logging
import time
from datetime import datetime, timedelta

import requests_cache

from acapi2.exceptions import AcquiaCloudTaskFailedException
from acapi2.resources.acquiaresource import AcquiaResource

LOGGER = logging.getLogger("acapi2.resources.task")


class Task(AcquiaResource):
    """
    Task is deprecated, let's not use it anymore.
    """

    POLL_INTERVAL = 3

    def mangle_uri(self, uri: str, task_data: dict):
        raise NotImplementedError

    def is_pending(self) -> bool:
        with requests_cache.disabled():
            tasks = self.request().json()["embedded"]["_items"]

        self.data = tasks[self.__getitem__("uuid")]
        return self.data["status"] != "in-progress"

    def wait(self, timeout: int = 1000) -> "Task":
        start = datetime.now()
        max_time = start + timedelta(seconds=timeout)

        while self.is_pending():
            if start >= max_time:
                msg = (
                    f"Time out exceeded while "
                    f"waiting for {self.data['uuid']}"
                )
                raise AcquiaCloudTaskFailedException(msg, self.data)
            time.sleep(self.POLL_INTERVAL)

        task = self.data
        if task["status"] == "failed":
            msg = f"Task {self.data['uuid']} failed"
            raise AcquiaCloudTaskFailedException(msg, task)

        end = datetime.now()
        delta = end - start

        LOGGER.info(
            "Waited %.2f seconds for task to complete", delta.total_seconds()
        )

        return self
