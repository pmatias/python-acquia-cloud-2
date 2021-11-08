#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia Cloud API task resources."""

from acapi2.resources.acquialist import AcquiaList
from acapi2.resources.task import Task


class TaskList(AcquiaList):
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
        self._filters = filters
        self.fetch()

    def fetch(self) -> None:
        tasks = self.request(uri=self.uri, params=self._filters).json()
        try:
            task_items = tasks["_embedded"]["items"]
        except KeyError:
            # TODO Handle this
            pass
        else:
            for task in task_items:
                task_id = task["uuid"]
                self.__setitem__(
                    task_id, Task(self.uri, self.api_key, self.api_secret)
                )
                loaded_task = self.__getitem__(task_id)
                loaded_task.data = task

    @property
    def base_uri(self) -> str:
        return self._base_uri

    @base_uri.setter
    def base_uri(self, base_uri: str):
        self._base_uri = f"{base_uri}/tasks"
