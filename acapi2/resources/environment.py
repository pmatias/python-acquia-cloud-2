#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Environment resource"""

from acapi2.resources.acquiaresource import AcquiaResource


class Environment(AcquiaResource):

    def destroy(self):
        raise NotImplementedError
