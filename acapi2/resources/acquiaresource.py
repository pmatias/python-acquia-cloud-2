#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Acquia Cloud API resource base."""

from acapi2.resources.acquiadata import AcquiaData


class AcquiaResource(AcquiaData):

    def __getitem__(self, item):
        print("OH HAI MARK!", item)
        exit(9)

    def get(self):
        if self.data is None:
            response = self.request()
            #self.data = response

        return self.data
