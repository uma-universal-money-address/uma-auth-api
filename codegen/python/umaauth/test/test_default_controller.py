import unittest

from flask import json

from umaauth.models.execute_quote_request import ExecuteQuoteRequest  # noqa: E501
from umaauth.models.execute_quote_response import ExecuteQuoteResponse  # noqa: E501
from umaauth.models.get_balance_request import GetBalanceRequest  # noqa: E501
from umaauth.models.get_balance_response import GetBalanceResponse  # noqa: E501
from umaauth.models.get_info_response import GetInfoResponse  # noqa: E501
from umaauth.models.invoice import Invoice  # noqa: E501
from umaauth.models.lookup_user_response import LookupUserResponse  # noqa: E501
from umaauth.models.make_invoice_request import MakeInvoiceRequest  # noqa: E501
from umaauth.models.pay_invoice_request import PayInvoiceRequest  # noqa: E501
from umaauth.models.pay_invoice_response import PayInvoiceResponse  # noqa: E501
from umaauth.models.pay_to_address_request import PayToAddressRequest  # noqa: E501
from umaauth.models.pay_to_address_response import PayToAddressResponse  # noqa: E501
from umaauth.models.quote import Quote  # noqa: E501
from umaauth.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_execute_quote(self):
        """Test case for execute_quote

        execute_quote: Execute a quote
        """
        execute_quote_request = {"payment_hash":"f1d2d2f924e986ac86fdf7b36c94bcdf32beec15"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/quote',
            method='POST',
            headers=headers,
            data=json.dumps(execute_quote_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fetch_quote(self):
        """Test case for fetch_quote

        fetch_quote: Get a quote for a payment
        """
        query_string = [('sending_currency_code', 'MXN'),
                        ('receiving_currency_code', 'USD'),
                        ('locked_currency_amount', 1000),
                        ('locked_currency_side', 'sending'),
                        ('receiving_address', '$alice@vasp.net')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/quote',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_balance(self):
        """Test case for get_balance

        get_balance: Get the balance of the user's wallet
        """
        get_balance_request = {"currency_code":"USD"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/balance',
            method='GET',
            headers=headers,
            data=json.dumps(get_balance_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_info(self):
        """Test case for get_info

        get_info: Get information about the user's wallet connection
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/info',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_lookup_invoice(self):
        """Test case for lookup_invoice

        lookup_invoice: Get an invoice by its payment hash
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/invoices/{payment_hash}'.format(payment_hash='f1d2d2f924e986ac86fdf7b36c94bcdf32beec15'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_lookup_user(self):
        """Test case for lookup_user

        lookup_user: Get receiver info by UMA
        """
        query_string = [('base_sending_currency_code', 'USD')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/receiver/uma/{receiver_uma}'.format(receiver_uma='$alice@vasp.net'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_make_invoice(self):
        """Test case for make_invoice

        make_invoice: Create a new invoice
        """
        make_invoice_request = {"amount":1000,"description_hash":"f1d2d2f924e986ac86fdf7b36c94bcdf32beec15","description":"Payment for services rendered.","expiry":3600}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/invoice',
            method='POST',
            headers=headers,
            data=json.dumps(make_invoice_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pay_invoice(self):
        """Test case for pay_invoice

        pay_invoice: Pay a bolt11 invoice
        """
        pay_invoice_request = {"amount":1000,"invoice":"lntb1u1pw0k7jw"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/payments/bolt11',
            method='POST',
            headers=headers,
            data=json.dumps(pay_invoice_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pay_to_address(self):
        """Test case for pay_to_address

        pay_to_address: Pay to an LNURL address
        """
        pay_to_address_request = {"sending_currency_code":"MXN","receiving_currency_code":"USD","receiver_address":"$alice@vasp.net","sending_currency_amount":1000}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/payments/lnurl',
            method='POST',
            headers=headers,
            data=json.dumps(pay_to_address_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
