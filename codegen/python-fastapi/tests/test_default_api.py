# coding: utf-8

from fastapi.testclient import TestClient


from uma_auth.models.execute_quote_request import ExecuteQuoteRequest  # noqa: F401
from uma_auth.models.execute_quote_response import ExecuteQuoteResponse  # noqa: F401
from uma_auth.models.get_balance_response import GetBalanceResponse  # noqa: F401
from uma_auth.models.get_info_response import GetInfoResponse  # noqa: F401
from uma_auth.models.invoice import Invoice  # noqa: F401
from uma_auth.models.lookup_user_response import LookupUserResponse  # noqa: F401
from uma_auth.models.make_invoice_request import MakeInvoiceRequest  # noqa: F401
from uma_auth.models.pay_invoice_request import PayInvoiceRequest  # noqa: F401
from uma_auth.models.pay_invoice_response import PayInvoiceResponse  # noqa: F401
from uma_auth.models.pay_to_address_request import PayToAddressRequest  # noqa: F401
from uma_auth.models.pay_to_address_response import PayToAddressResponse  # noqa: F401
from uma_auth.models.quote import Quote  # noqa: F401


def test_execute_quote(client: TestClient):
    """Test case for execute_quote

    execute_quote: Execute a quote
    """
    execute_quote_request = {"payment_hash":"f1d2d2f924e986ac86fdf7b36c94bcdf32beec15"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/quote",
    #    headers=headers,
    #    json=execute_quote_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_fetch_quote(client: TestClient):
    """Test case for fetch_quote

    fetch_quote: Get a quote for a payment
    """
    params = [("sending_currency_code", 'MXN'),     ("receiving_currency_code", 'USD'),     ("locked_currency_amount", 1000),     ("locked_currency_side", 'sending'),     ("receiving_address", '$alice@vasp.net')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/quote",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_balance(client: TestClient):
    """Test case for get_balance

    get_balance: Get the balance of the user's wallet
    """
    params = [("currency_code", 'USD')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/balance",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_info(client: TestClient):
    """Test case for get_info

    get_info: Get information about the user's wallet connection
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/info",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_lookup_invoice(client: TestClient):
    """Test case for lookup_invoice

    lookup_invoice: Get an invoice by its payment hash
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/invoices/{payment_hash}".format(payment_hash='f1d2d2f924e986ac86fdf7b36c94bcdf32beec15'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_lookup_user(client: TestClient):
    """Test case for lookup_user

    lookup_user: Get receiver info by UMA
    """
    params = [("base_sending_currency_code", 'USD')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/receiver/uma/{receiver_uma}".format(receiver_uma='$alice@vasp.net'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_make_invoice(client: TestClient):
    """Test case for make_invoice

    make_invoice: Create a new invoice
    """
    make_invoice_request = {"amount":1000,"description_hash":"f1d2d2f924e986ac86fdf7b36c94bcdf32beec15","description":"Payment for services rendered.","expiry":3600}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/invoice",
    #    headers=headers,
    #    json=make_invoice_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_pay_invoice(client: TestClient):
    """Test case for pay_invoice

    pay_invoice: Pay a bolt11 invoice
    """
    pay_invoice_request = {"amount":1000,"invoice":"lntb1u1pw0k7jw"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/payments/bolt11",
    #    headers=headers,
    #    json=pay_invoice_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_pay_to_address(client: TestClient):
    """Test case for pay_to_address

    pay_to_address: Pay to an LNURL address
    """
    pay_to_address_request = {"sending_currency_code":"MXN","receiving_currency_code":"USD","receiver_address":"$alice@vasp.net","sending_currency_amount":1000}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/payments/lnurl",
    #    headers=headers,
    #    json=pay_to_address_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

