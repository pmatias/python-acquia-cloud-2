#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia Cloud API Exceptions"""

from pprint import pformat


class AcquiaCloudException(Exception):
    """Generic Acquia Cloud API Exception.

    All acapi2 exceptions should extend this class.
    """


class AcquiaCloudNoDataException(AcquiaCloudException):
    """No data found exception."""


class AcquiaCloudNotificationException(AcquiaCloudException):
    """An Acquia notification exception."""

    def __init__(self, message, task):
        """Constructor.

        Parameters
        ----------
        message: str
            The error message.
        task: Task
            The Task object for the task that failed.
        """
        super().__init__(message)
        self.message = message
        self.task = task

    def __str__(self):
        """Return the string representation of the exception.

        Returns
        -------
        str
            The error message and pretty printed Task object properties.
        """
        task = pformat(self.task, indent=4)
        return f"{self.message}\n{task}"


class AcquiaCloudTaskFailedException(AcquiaCloudNotificationException):
    """An Acquia task failure exception."""


class AcquiaCloudNotificationFailedException(AcquiaCloudNotificationException):
    """An Acquia notification failure exception."""


class AcquiaCloudTimeoutError(AcquiaCloudNotificationException):
    """Timeout exceeded error."""
