# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.account import Account  # noqa: E501
from swagger_server.models.deal import Deal  # noqa: E501
from swagger_server.models.debt import Debt  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server.models.transfer import Transfer  # noqa: E501
from swagger_server.test import BaseTestCase


class TestApiController(BaseTestCase):
    """ApiController integration test stubs"""

    def test_add_account(self):
        """Test case for add_account

        Add a new account to the store
        """
        body = Account("test")
        response = self.client.open(
            '/api/addAccount',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_deal(self):
        """Test case for add_deal

        Add a new deal to the store
        """
        body = Deal("test", "test", "test", ["test"], 32, "test")
        response = self.client.open(
            '/api/addDeal',
            method='POST',
            data=json.dumps(body.to_dict()),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_person(self):
        """Test case for add_person

        Add a new person to the store
        """
        body = Person("test", "test")
        response = self.client.open(
            '/api/addPerson',
            method='POST',
            data=json.dumps(body.to_dict()),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_transfer(self):
        """Test case for add_transfer

        Add a new transfer to the store
        """
        body = Transfer("test", "test", "test", 32, "test")
        response = self.client.open(
            '/api/addTransfer',
            method='POST',
            data=json.dumps(body.to_dict()),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_accounts(self):
        """Test case for get_accounts

        Finds Accounts by accountId
        """
        query_string = [('accountId', 'test')]
        response = self.client.open(
            '/api/getAccounts',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_deals(self):
        """Test case for get_deals

        Finds deals by accountId
        """
        query_string = [('accountId', 'test')]
        response = self.client.open(
            '/api/getDeals',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_debts(self):
        """Test case for get_debts

        Finds debts by accountId
        """
        query_string = [('accountId', 'test')]
        response = self.client.open(
            '/api/getDebts',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_persons(self):
        """Test case for get_persons

        Finds Persons by accountId
        """
        query_string = [('accountId', 'test')]
        response = self.client.open(
            '/api/getPersons',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_transfers(self):
        """Test case for get_transfers

        Finds Transfers by accountId
        """
        query_string = [('accountId', 'test')]
        response = self.client.open(
            '/api/getTransfers',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
