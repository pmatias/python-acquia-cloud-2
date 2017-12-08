#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia Cloud API resource base."""

from acapi2.resources.acquiadata import AcquiaData


class AcquiaResource(AcquiaData):

    def __getitem__(self, key):
        if not self.data:
            self.get()

        return self.data[key]

    def get(self):
        if not self.data:
            response = self.request()
            self.data = response.content

        return self.data
