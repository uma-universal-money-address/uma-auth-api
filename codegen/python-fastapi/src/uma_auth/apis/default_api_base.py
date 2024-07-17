# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from uma_auth.models.execute_quote_request import ExecuteQuoteRequest
from uma_auth.models.execute_quote_response import ExecuteQuoteResponse
from uma_auth.models.get_balance_response import GetBalanceResponse
from uma_auth.models.get_info_response import GetInfoResponse
from uma_auth.models.invoice import Invoice
from uma_auth.models.lookup_user_response import LookupUserResponse
from uma_auth.models.make_invoice_request import MakeInvoiceRequest
from uma_auth.models.pay_invoice_request import PayInvoiceRequest
from uma_auth.models.pay_invoice_response import PayInvoiceResponse
from uma_auth.models.pay_to_address_request import PayToAddressRequest
from uma_auth.models.pay_to_address_response import PayToAddressResponse
from uma_auth.models.quote import Quote


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    def execute_quote(
        self,
        execute_quote_request: ExecuteQuoteRequest,
    ) -> ExecuteQuoteResponse:
        ...


    def fetch_quote(
        self,
        sending_currency_code: str,
        receiving_currency_code: str,
        locked_currency_amount: int,
        locked_currency_side: str,
        receiving_address: str,
    ) -> Quote:
        ...


    def get_balance(
        self,
        currency_code: str,
    ) -> GetBalanceResponse:
        ...


    def get_info(
        self,
    ) -> GetInfoResponse:
        ...


    def lookup_invoice(
        self,
        payment_hash: str,
    ) -> Invoice:
        ...


    def lookup_user(
        self,
        receiver_uma: str,
        base_sending_currency_code: str,
    ) -> LookupUserResponse:
        ...


    def make_invoice(
        self,
        make_invoice_request: MakeInvoiceRequest,
    ) -> Invoice:
        ...


    def pay_invoice(
        self,
        pay_invoice_request: PayInvoiceRequest,
    ) -> PayInvoiceResponse:
        ...


    def pay_to_address(
        self,
        pay_to_address_request: PayToAddressRequest,
    ) -> PayToAddressResponse:
        ...
