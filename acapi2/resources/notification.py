#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Notification object"""


import logging
import time
from datetime import datetime, timedelta

import requests_cache

from acapi2.exceptions import (
    AcquiaCloudNotificationFailedException,
    AcquiaCloudTimeoutError,
)
from acapi2.resources.acquiaresource import AcquiaResource

LOGGER = logging.getLogger("acapi2.resources.notification")


class Notification(AcquiaResource):
    POLL_INTERVAL = 3

    def __init__(
        self,
        uri: str,
        api_key: str,
        api_secret: str,
        filters: dict = None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(uri, api_key, api_secret, *args, **kwargs)

    def pending(self) -> bool:
        """Check if a notification is still pending.

        :return: is the notification task in progress or no
        """
        with requests_cache.disabled():
            notification = self.request().json()
        self.data = notification
        return notification["status"] == "in-progress"

    def wait(self, timeout: int = 1800) -> "Notification":
        """Wait for a notification task to finish executing.

        :param timeout: the max number of seconds to wait for the notification
                        to complete
        :return: Notification object or raise exceptions
        """
        start = datetime.now()
        max_time = start + timedelta(seconds=timeout)
        while self.pending():
            # Ensure the timeout hasn't been exceeded.
            if datetime.now() >= max_time:
                msg = (
                    f"Time out of exceeded while waiting "
                    f"for {self.data['uuid']}"
                )
                raise AcquiaCloudTimeoutError(msg, self.data)
            time.sleep(self.POLL_INTERVAL)

        # Grab the cached response
        notification = self.data
        if notification["status"] in ["failed", "error"]:
            raise AcquiaCloudNotificationFailedException(
                f"Notification {notification['uuid']} failed", notification
            )

        end = datetime.now()
        delta = end - start
        LOGGER.info(
            "Waited %.2f seconds for notification to complete",
            delta.total_seconds(),
        )

        return self
