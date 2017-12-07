#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia Cloud API task resources."""

from acapi2.resources.acquialist import AcquiaList
from acapi2.resources.task import Task


class TaskList(AcquiaList):
    def __init__(self, base_uri: str, api_key: str, api_secret: str,
                 *args, **kwargs):
        super().__init__(base_uri, api_key, api_secret, *args,
                         **kwargs)
        self.fetch()

    def fetch(self) -> None:
        tasks = super().request(uri=self.uri).json()
        try:
            task_items = tasks["_embedded"]["items"]
        except KeyError:
            # TODO Handle this
            pass
        else:
            for task in task_items:
                task_id = task["uuid"]
                subs_uri = "{base_uri}/{uuid}".format(
                    base_uri=self.uri, uuid=task_id)
                self.__setitem__(task_id,
                                 Task(subs_uri,
                                      self.api_key,
                                      self.api_secret))

    @property
    def base_uri(self) -> str:
        return self._base_uri

    @base_uri.setter
    def base_uri(self, base_uri: str):
        uri = "{}/tasks".format(base_uri)
        self._base_uri = uri
