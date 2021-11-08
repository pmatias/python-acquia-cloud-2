#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Dictionary of Acquia Cloud API resources."""
import abc
import typing

from acapi2.exceptions import AcquiaCloudNoDataException
from acapi2.resources.acquiadata import AcquiaData


class AcquiaList(AcquiaData, dict):
    def __init__(
        self, base_uri: str, api_key: str, api_secret: str, *args, **kwargs
    ) -> None:
        self._sorted_keys = []  # type: typing.List[typing.Any]

        # Initialise the dict
        dict.__init__(self, *args, **kwargs)

        # Initialise the list
        self._base_uri: str = ""
        self.base_uri: str = base_uri  # type: ignore
        AcquiaData.__init__(self, self.base_uri, api_key, api_secret)

    def __delitem__(self, key):
        super(AcquiaList, self).__delitem__(key)
        self.sorted_keys = []

    def __setitem__(self, key, value):
        super(AcquiaList, self).__setitem__(key, value)
        self.sorted_keys = []

    def first(self) -> typing.Any:
        if not len(self):
            raise AcquiaCloudNoDataException("No data available.")

        key = self.search_pos(0)
        return self[key]

    def generate_resource_uri(self, resource: str) -> str:
        return f"{self.base_uri}/{resource}"

    def last(self):
        if not len(self):
            raise AcquiaCloudNoDataException("No data available.")

        key = self.search_pos(-1)
        return self[key]

    def search_pos(self, pos: int) -> str:
        keys = self.sorted_keys
        return keys[pos]

    @property
    def sorted_keys(self) -> list:
        if not self._sorted_keys:
            keys = list(self.keys())
            self._sorted_keys = sorted(keys)

        return self._sorted_keys

    @sorted_keys.setter
    def sorted_keys(self, keys: list):
        self._sorted_keys = keys

    @property  # type: ignore
    @abc.abstractmethod
    def base_uri(self) -> str:
        return self._base_uri

    @base_uri.setter  # type: ignore
    @abc.abstractmethod
    def base_uri(self, base_uri: str):
        self._base_uri = base_uri
