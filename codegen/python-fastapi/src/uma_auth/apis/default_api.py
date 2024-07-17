# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from uma_auth.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from uma_auth.models.extra_models import TokenModel  # noqa: F401
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


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/quote",
    responses={
        200: {"model": ExecuteQuoteResponse, "description": "OK"},
    },
    tags=["default"],
    summary="execute_quote: Execute a quote",
    response_model_by_alias=True,
)
async def execute_quote(
    execute_quote_request: ExecuteQuoteRequest = Body(None, description=""),
) -> ExecuteQuoteResponse:
    ...


@router.get(
    "/quote",
    responses={
        200: {"model": Quote, "description": "OK"},
    },
    tags=["default"],
    summary="fetch_quote: Get a quote for a payment",
    response_model_by_alias=True,
)
async def fetch_quote(
    sending_currency_code: str = Query(None, description="The currency code being sent from the sender&#39;s wallet.", alias="sending_currency_code"),
    receiving_currency_code: str = Query(None, description="The currency code of the currency that the receiver will receive.", alias="receiving_currency_code"),
    locked_currency_amount: int = Query(None, description="The amount to send/receive in the smallest unit of the locked currency (eg. cents). See &#x60;locked_currency_side&#x60; for more information.", alias="locked_currency_amount"),
    locked_currency_side: str = Query(None, description="The side of the quote which should be locked and specified in the &#x60;locked_currency_amount&#x60;. For example, if I want to send exactly $5 MXN from my wallet, I would set this to \&quot;sending\&quot;, and the &#x60;locked_currency_amount&#x60; to 500 (in cents). If I want the receiver to receive exactly $10 USD, I would set this to \&quot;receiving\&quot; and the &#x60;locked_currency_amount&#x60; to 10000 (in cents).", alias="locked_currency_side"),
    receiving_address: str = Query(None, description="The UMA address to send the payment to.", alias="receiving_address"),
) -> Quote:
    ...


@router.get(
    "/balance",
    responses={
        200: {"model": GetBalanceResponse, "description": "OK"},
    },
    tags=["default"],
    summary="get_balance: Get the balance of the user&#39;s wallet",
    response_model_by_alias=True,
)
async def get_balance(
    currency_code: str = Query(None, description="The currency code of the balance. Assumed to be in msats if not provided. ", alias="currency_code"),
) -> GetBalanceResponse:
    ...


@router.get(
    "/info",
    responses={
        200: {"model": GetInfoResponse, "description": "OK"},
    },
    tags=["default"],
    summary="get_info: Get information about the user&#39;s wallet connection",
    response_model_by_alias=True,
)
async def get_info(
) -> GetInfoResponse:
    ...


@router.get(
    "/invoices/{payment_hash}",
    responses={
        200: {"model": Invoice, "description": "OK"},
    },
    tags=["default"],
    summary="lookup_invoice: Get an invoice by its payment hash",
    response_model_by_alias=True,
)
async def lookup_invoice(
    payment_hash: str = Path(..., description="The payment hash of the invoice."),
) -> Invoice:
    ...


@router.get(
    "/receiver/uma/{receiver_uma}",
    responses={
        200: {"model": LookupUserResponse, "description": "OK"},
    },
    tags=["default"],
    summary="lookup_user: Get receiver info by UMA",
    response_model_by_alias=True,
)
async def lookup_user(
    receiver_uma: str = Path(..., description="The receiver&#39;s UMA."),
    base_sending_currency_code: str = Query(None, description="The currency code of the sender&#39;s balance. Assumed to be in msats if not provided.  This is used to calculate the multiplier for the receiver&#39;s currencies.", alias="base_sending_currency_code"),
) -> LookupUserResponse:
    ...


@router.post(
    "/invoice",
    responses={
        200: {"model": Invoice, "description": "OK"},
    },
    tags=["default"],
    summary="make_invoice: Create a new invoice",
    response_model_by_alias=True,
)
async def make_invoice(
    make_invoice_request: MakeInvoiceRequest = Body(None, description=""),
) -> Invoice:
    ...


@router.post(
    "/payments/bolt11",
    responses={
        200: {"model": PayInvoiceResponse, "description": "OK"},
    },
    tags=["default"],
    summary="pay_invoice: Pay a bolt11 invoice",
    response_model_by_alias=True,
)
async def pay_invoice(
    pay_invoice_request: PayInvoiceRequest = Body(None, description=""),
) -> PayInvoiceResponse:
    ...


@router.post(
    "/payments/lnurl",
    responses={
        200: {"model": PayToAddressResponse, "description": "OK"},
    },
    tags=["default"],
    summary="pay_to_address: Pay to an LNURL address",
    response_model_by_alias=True,
)
async def pay_to_address(
    pay_to_address_request: PayToAddressRequest = Body(None, description=""),
) -> PayToAddressResponse:
    ...
