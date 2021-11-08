#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from acapi2.resources.acquiaresource import AcquiaResource
from acapi2.resources.applicationlist import ApplicationList


class Subscription(AcquiaResource):
    def applications(self):
        applications = ApplicationList(self.uri, self.api_key, self.api_secret)
        return applications

    def entitlements(self):
        raise NotImplementedError
