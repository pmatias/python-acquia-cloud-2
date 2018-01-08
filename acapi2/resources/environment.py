#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Environment resource"""

from acapi2.resources.acquiaresource import AcquiaResource
from requests.sessions import Session
from requests.exceptions import RequestException

class Environment(AcquiaResource):

    def destroy(self):
        response = self.request(uri=self.uri, method="DELETE")

        return response

    def code_switch(self, branch: str) -> Session:
        uri = self.uri + "/code/actions/switch"
        data = {
            "branch": branch
        }

        try:
            response = self.request(uri=uri, method="POST", data=data)
        except RequestException:
            print("There was an error on the request")
        else:
            return response