#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia Cloud API resource base."""

from acapi2.resources.acquiadata import AcquiaData


class AcquiaResource(AcquiaData):
    def __getitem__(self, key):
        if not key and not self.data:
            self.populate_data()

        return self.data[key]

    @property
    def data(self):
        if not self._data:
            self.populate_data()
        return self._data

    @data.setter
    def data(self, data: dict):
        self._data = data

    def populate_data(self) -> None:
        results = self.request().json()
        self.data = results
