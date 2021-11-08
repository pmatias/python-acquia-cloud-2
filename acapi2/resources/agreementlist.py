#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Agreement list"""

from acapi2.exceptions import AcquiaCloudNoDataException
from acapi2.resources.acquialist import AcquiaList
from acapi2.resources.agreement import Agreement


class AgreementList(AcquiaList):
    def __init__(
        self, uri: str, api_key: str, api_secret: str, *args, **kwargs
    ) -> None:

        super().__init__(uri, api_key, api_secret, *args, **kwargs)
        self.fetch()

    def fetch(self) -> None:
        agreements = self.request(uri=self.uri).json()
        try:
            agr_items = agreements["_embedded"]["items"]
        except KeyError:
            raise AcquiaCloudNoDataException()
        else:
            for agreement in agr_items:
                agr_uri = agreement["_links"]["self"]["href"]
                self.__setitem__(
                    agreement["uuid"],
                    Agreement(agr_uri, self.api_key, self.api_secret),
                )

    @property
    def base_uri(self) -> str:
        return self._base_uri

    @base_uri.setter
    def base_uri(self, base_uri: str):
        self._base_uri = f"{base_uri}/agreements"
