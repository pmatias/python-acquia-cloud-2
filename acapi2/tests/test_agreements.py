#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Agreements tests"""

import requests_mock

from acapi2.resources.agreement import Agreement
from acapi2.resources.agreementlist import AgreementList
from acapi2.tests import BaseTest


@requests_mock.Mocker()
class TestAgreements(BaseTest):
    def test_agreement_list(self, mocker):
        response = {
            "total": 3,
            "_links": {
                "self": {"href": "https://cloud.acquia.com/api/agreements"},
                "parent": {"href": "https://cloud.acquia.com/api/"},
            },
            "_embedded": {
                "items": [
                    {
                        "uuid": "efc62c93-8203-4e8b-a8ff-4d18b780d4ab",
                        "document_uuid": "f25d0284-f25f-4e59-"
                        "9c48-7c39ae57b400",
                        "title": "Agreement Title",
                        "body": "<p>Agreement body and text.</p>",
                        "status": "accepted",
                        "created_at": "2017-01-23T12:00:00Z",
                        "updated_at": "2017-01-27T12:00:00Z",
                        "actioned_by": {
                            "uuid": "5aa902c5-f1c1-6c94-edfa-86bc58d0dce3",
                            "first_name": "James",
                            "last_name": "Kirk",
                            "mail": "james.kirk@example.com",
                            "picture_url": "https://accounts.acquia.com/sites"
                            "/default/avatars/456def"
                            "?mail=james.kirk"
                            "@example.com",
                            "username": "james.kirk",
                        },
                        "reference": {
                            "uuid": "9ab09eba-290d-4ed9-be4d-fa194ab92f39",
                            "name": "Acquia Subscription",
                            "type": "subscription",
                        },
                        "_links": {
                            "self": {
                                "href": "https://cloud.acquia.com/api"
                                "/agreements/efc62c93-8203-4e8b-"
                                "a8ff-4d18b780d4ab"
                            }
                        },
                    },
                    {
                        "uuid": "b63fff64-6c18-4899-acba-00ec6c8930e9",
                        "title": "Another Agreement",
                        "body": "<p>This is the body and text of another "
                        "agreement.</p>",
                        "status": "declined",
                        "created_at": "2017-02-23T12:00:00Z",
                        "updated_at": "2017-02-27T12:00:00Z",
                        "actioned_by": {
                            "uuid": "550e8400-e29b-41d4-a716-446655440000",
                            "first_name": "Jane",
                            "last_name": "Doe",
                            "mail": "jane.doe@example.com",
                            "picture_url": "https://accounts.acquia.com/"
                            "sites/default/avatars/123abc?"
                            "mail=jane.doe"
                            "@example.com",
                            "username": "jane.doe",
                        },
                        "reference": {
                            "uuid": "9ab09eba-290d-4ed9-be4d-fa194ab92f39",
                            "name": "Acquia Subscription",
                            "type": "subscription",
                        },
                        "_links": {
                            "self": {
                                "href": "https://cloud.acquia.com/api/"
                                "agreements/b63fff64-6c18-4899-acba-"
                                "00ec6c8930e9"
                            }
                        },
                    },
                    {
                        "uuid": "a8777880-8924-494a-abe2-62cc092df269",
                        "title": "A Third Agreement",
                        "body": "<p>This is the body and text of one "
                        "more agreement.</p>",
                        "status": "pending",
                        "created_at": "2017-02-23T12:00:00Z",
                        "updated_at": None,
                        "actioned_by": None,
                        "reference": {
                            "uuid": "9ab09eba-290d-4ed9-be4d-fa194ab92f39",
                            "name": "Acquia Subscription",
                            "type": "subscription",
                        },
                        "_links": {
                            "self": {
                                "href": "https://cloud.acquia.com/api/"
                                "agreements/a8777880-8924-494a-"
                                "abe2-62cc092df269"
                            }
                        },
                    },
                ]
            },
        }

        uri = f"{self.endpoint}/agreements"
        mocker.register_uri("GET", uri, json=response, status_code=200)

        agrs = self.acquia.agreements()
        self.assertIsInstance(agrs, AgreementList)

    def test_agreement(self, mocker):
        uuid = "efc62c93-8203-4e8b-a8ff-4d18b780d4ab"
        response = {
            "uuid": uuid,
            "document_uuid": "f25d0284-f25f-4e59-9c48-7c39ae57b400",
            "title": "Agreement Title",
            "body": "<p>Agreement body and text.</p>",
            "status": "accepted",
            "created_at": "2017-01-23T12:00:00Z",
            "updated_at": "2017-01-27T12:00:00Z",
            "actioned_by": {
                "uuid": "5aa902c5-f1c1-6c94-edfa-86bc58d0dce3",
                "first_name": "James",
                "last_name": "Kirk",
                "mail": "james.kirk@example.com",
                "picture_url": "https://accounts.acquia.com/sites/default/"
                "avatars/456def?mail=james.kirk@example.com",
                "username": "james.kirk",
            },
            "reference": {
                "uuid": "9ab09eba-290d-4ed9-be4d-fa194ab92f39",
                "name": "Acquia Subscription",
                "type": "subscription",
            },
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/agreements/"
                    "efc62c93-8203-4e8b-a8ff-4d18b780d4ab"
                },
                "invitees": {
                    "href": "https://cloud.acquia.com/api/agreements/"
                    "efc62c93-8203-4e8b-a8ff-4d18b780d4ab/invitees"
                },
                "subscription": {
                    "href": "https://cloud.acquia.com/api/subscriptions/"
                    "9ab09eba-290d-4ed9-be4d-fa194ab92f39"
                },
                "actioned_by": {
                    "href": "https://cloud.acquia.com/api/users/"
                    "5aa902c5-f1c1-6c94-edfa-86bc58d0dce3"
                },
                "parent": {"href": "https://cloud.acquia.com/api/agreements"},
            },
        }

        uri = f"{self.endpoint}/agreements/{uuid}"
        mocker.register_uri("GET", uri, json=response, status_code=200)
        agreement = self.acquia.agreement(uuid)
        self.assertIsInstance(agreement, Agreement)

    def test_accept_agreement(self, mocker):
        response = {"message": "The agreement has been accepted."}
        uuid = "efc62c93-8203-4e8b-a8ff-4d18b780d4ab"
        uri = f"{self.endpoint}/agreements/{uuid}/actions/accept"
        mocker.register_uri(
            url=uri, method="POST", status_code=200, json=response
        )

        response = self.acquia.agreement(uuid).accept()
        self.assertEqual(response.status_code, 200)

    def test_decline_agreement(self, mocker):
        response = {"message": "The agreement has been declined."}
        uuid = "efc62c93-8203-4e8b-a8ff-4d18b780d4ab"
        uri = f"{self.endpoint}/agreements/{uuid}/actions/decline"
        mocker.register_uri(
            url=uri, method="POST", status_code=200, json=response
        )

        response = self.acquia.agreement(uuid).decline()
        self.assertEqual(response.status_code, 200)

    def test_agreement_invitees(self, mocker):
        response = {
            "total": 2,
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.com/api/agreements/"
                    "efc62c93-8203-4e8b-a8ff-4d18b780d4ab/invitees"
                },
                "parent": {
                    "href": "https://cloud.acquia.com/api/agreements/"
                    "efc62c93-8203-4e8b-a8ff-4d18b780d4ab"
                },
            },
            "_embedded": {
                "items": [
                    {
                        "uuid": "u4ee550f-ee0c-102e-8305-1231390f2cc1",
                        "first_name": "User",
                        "last_name": "One",
                        "mail": "user1@example.com",
                        "username": "user.one",
                        "picture_url": "https://accounts.acquia.com/"
                        "path/to/image.png",
                    },
                    {
                        "uuid": "u4ef8edc-ee0c-102e-8305-1231390f2cc2",
                        "first_name": "User",
                        "last_name": "Two",
                        "mail": "user2@example.com",
                        "username": "user.two",
                        "picture_url": "https://accounts.acquia.com/"
                        "path/to/image.png",
                    },
                ]
            },
        }
        uuid = "efc62c93-8203-4e8b-a8ff-4d18b780d4ab"

        uri = f"{self.endpoint}/agreements/{uuid}/invitees"
        mocker.register_uri("GET", uri, json=response, status_code=200)

        invitees_response = self.acquia.agreement(uuid).invitees()

        self.assertIn("total", invitees_response)
