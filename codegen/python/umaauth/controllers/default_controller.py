import connexion
from typing import Dict
from typing import Tuple
from typing import Union

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
from umaauth import util


def execute_quote(execute_quote_request=None):  # noqa: E501
    """execute_quote: Execute a quote

     # noqa: E501

    :param execute_quote_request: 
    :type execute_quote_request: dict | bytes

    :rtype: Union[ExecuteQuoteResponse, Tuple[ExecuteQuoteResponse, int], Tuple[ExecuteQuoteResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        execute_quote_request = ExecuteQuoteRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def fetch_quote(sending_currency_code, receiving_currency_code, locked_currency_amount, locked_currency_side, receiving_address):  # noqa: E501
    """fetch_quote: Get a quote for a payment

     # noqa: E501

    :param sending_currency_code: The currency code being sent from the sender&#39;s wallet.
    :type sending_currency_code: str
    :param receiving_currency_code: The currency code of the currency that the receiver will receive.
    :type receiving_currency_code: str
    :param locked_currency_amount: The amount to send/receive in the smallest unit of the locked currency (eg. cents). See &#x60;locked_currency_side&#x60; for more information.
    :type locked_currency_amount: 
    :param locked_currency_side: The side of the quote which should be locked and specified in the &#x60;locked_currency_amount&#x60;. For example, if I want to send exactly $5 MXN from my wallet, I would set this to \&quot;sending\&quot;, and the &#x60;locked_currency_amount&#x60; to 500 (in cents). If I want the receiver to receive exactly $10 USD, I would set this to \&quot;receiving\&quot; and the &#x60;locked_currency_amount&#x60; to 10000 (in cents).
    :type locked_currency_side: str
    :param receiving_address: The UMA address to send the payment to.
    :type receiving_address: str

    :rtype: Union[Quote, Tuple[Quote, int], Tuple[Quote, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_balance(get_balance_request=None):  # noqa: E501
    """get_balance: Get the balance of the user&#39;s wallet

     # noqa: E501

    :param get_balance_request: 
    :type get_balance_request: dict | bytes

    :rtype: Union[GetBalanceResponse, Tuple[GetBalanceResponse, int], Tuple[GetBalanceResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        get_balance_request = GetBalanceRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_info():  # noqa: E501
    """get_info: Get information about the user&#39;s wallet connection

     # noqa: E501


    :rtype: Union[GetInfoResponse, Tuple[GetInfoResponse, int], Tuple[GetInfoResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def lookup_invoice(payment_hash):  # noqa: E501
    """lookup_invoice: Get an invoice by its payment hash

     # noqa: E501

    :param payment_hash: The payment hash of the invoice.
    :type payment_hash: str

    :rtype: Union[Invoice, Tuple[Invoice, int], Tuple[Invoice, int, Dict[str, str]]
    """
    return 'do some magic!'


def lookup_user(receiver_uma, base_sending_currency_code=None):  # noqa: E501
    """lookup_user: Get receiver info by UMA

     # noqa: E501

    :param receiver_uma: The receiver&#39;s UMA.
    :type receiver_uma: str
    :param base_sending_currency_code: The currency code of the sender&#39;s balance. Assumed to be in msats if not provided.  This is used to calculate the multiplier for the receiver&#39;s currencies.
    :type base_sending_currency_code: str

    :rtype: Union[LookupUserResponse, Tuple[LookupUserResponse, int], Tuple[LookupUserResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def make_invoice(make_invoice_request=None):  # noqa: E501
    """make_invoice: Create a new invoice

     # noqa: E501

    :param make_invoice_request: 
    :type make_invoice_request: dict | bytes

    :rtype: Union[Invoice, Tuple[Invoice, int], Tuple[Invoice, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        make_invoice_request = MakeInvoiceRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def pay_invoice(pay_invoice_request=None):  # noqa: E501
    """pay_invoice: Pay a bolt11 invoice

     # noqa: E501

    :param pay_invoice_request: 
    :type pay_invoice_request: dict | bytes

    :rtype: Union[PayInvoiceResponse, Tuple[PayInvoiceResponse, int], Tuple[PayInvoiceResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        pay_invoice_request = PayInvoiceRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def pay_to_address(pay_to_address_request=None):  # noqa: E501
    """pay_to_address: Pay to an LNURL address

     # noqa: E501

    :param pay_to_address_request: 
    :type pay_to_address_request: dict | bytes

    :rtype: Union[PayToAddressResponse, Tuple[PayToAddressResponse, int], Tuple[PayToAddressResponse, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        pay_to_address_request = PayToAddressRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
