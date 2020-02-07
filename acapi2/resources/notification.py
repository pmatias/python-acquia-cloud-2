#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Notification object"""


import logging

from acapi2.resources.acquiaresource import AcquiaResource


LOGGER = logging.getLogger('acapi2.resources.notification')


class Notification(AcquiaResource):

    def __init__(self, uri: str,
                 api_key: str,
                 api_secret: str,
                 filters: dict = None,
                 *args, **kwargs) -> None:
        super().__init__(uri, api_key, api_secret, *args, **kwargs)
