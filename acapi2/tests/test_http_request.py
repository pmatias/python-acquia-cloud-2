#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unittest.mock import patch

from acapi2.http_request import HttpRequest
from acapi2.tests import BaseTest


class TestHttpRequest(BaseTest):
    def test_session(self):
        http_request = HttpRequest()
        http_request_1 = HttpRequest()
        self.assertEqual(id(http_request.session), id(http_request_1.session))

    def test_get_session(self):
        request_session = HttpRequest()._get_session()
        self.assertEqual(HttpRequest._session, request_session)

    @patch("requests.Session.request")
    def test_make_request(self, mock_session):
        http_request = HttpRequest()
        http_request.body = "body"
        http_request.do()
        mock_session.assert_called_once_with(
            "GET", "http://localhost/", data="body", headers={}
        )
