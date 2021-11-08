#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Agreement resource"""


from requests.exceptions import RequestException
from requests.sessions import Session

from acapi2.resources.acquiaresource import AcquiaResource


class Agreement(AcquiaResource):
    def __init__(
        self, uri: str, api_key: str, api_secret: str, *args, **kwargs
    ) -> None:
        super().__init__(uri, api_key, api_secret, *args, **kwargs)

    def accept(self) -> Session:
        """Accept a legal agreement by UUID."""
        uri = f"{self.uri}/actions/accept"
        response = Session()
        try:
            response = self.request(uri=uri, method="POST", data={})
        except RequestException:
            print("There was an error in the request.")

        return response

    def decline(self) -> Session:
        """Decline a legal agreement by UUID."""
        uri = f"{self.uri}/actions/decline"
        response = Session()
        try:
            response = self.request(uri=uri, method="POST", data={})
        except RequestException:
            print("There was an error in the request.")

        return response

    def invitees(self) -> Session:
        """Return a list of users invited to action this agreement."""
        uri = f"{self.uri}/invitees"
        return self.request(uri=uri).json()
