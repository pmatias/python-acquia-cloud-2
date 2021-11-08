"""Module contains http hmac request, supports HTTP persistent connection."""

import httphmac
import requests


class HttpRequest(httphmac.Request):
    """Class to represent HTTP keep-alive hmac Request."""

    _session = None

    def __init__(self):
        """Initialize HTTP Request object with requests.Session."""
        super().__init__()
        self.session = self._get_session()

    def _get_session(self):
        """Generate new session object.

        :return: requests.Session
        """
        if not HttpRequest._session:
            HttpRequest._session = requests.Session()
        return HttpRequest._session

    def do(self):
        """ "Executes the request represented by this object.

        The requests library will be used for this purpose.
        Use requests.Session object for reuse TCP connection.
        Returns an instance of requests.Response.
        """
        data = None
        if self.body is not None and self.body != b"":
            data = self.body
        return self.session.request(
            self.method, str(self.url), data=data, headers=self.header
        )
